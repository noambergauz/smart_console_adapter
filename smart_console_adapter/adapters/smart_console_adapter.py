import httpx


class SmartConsoleAdapter:
    def __init__(self, base_url: str, domain: str):
        self.base_url = base_url
        self.domain = domain
        self._headers = {
            "Content-Type": "application/json",
        }

    def set_sid(self, sid: str):
        """Set the session ID for subsequent requests."""
        self._headers["X-chkp-sid"] = sid

    async def login(self, user: str, password: str):
        """Login to the Smart Console and return the session ID."""
        url = f"{self.base_url}/login"
        async with httpx.AsyncClient(verify=False) as client:
            response = await client.post(
                url,
                json={"user": user, "password": password, "domain": self.domain},
                headers=self._headers,
            )
            response.raise_for_status()
            data = response.json()
            return data["sid"]

    async def show_users(self):
        """Get the list of users."""
        url = f"{self.base_url}/show-users"
        async with httpx.AsyncClient(verify=False) as client:
            response = await client.get(url, headers=self._headers)
            response.raise_for_status()
            return response.json()

    async def set_user(
        self, name: str, details_level: str = "full", expiration_days: int = 14
    ):
        """Set user details."""
        url = f"{self.base_url}/set-user"
        async with httpx.AsyncClient(verify=False) as client:
            response = await client.post(
                url,
                json={
                    "name": name,
                    "details-level": details_level,
                    "certificates": {
                        "add": {
                            "registration-key": {
                                "expiration-days": f"{expiration_days}"
                            }
                        }
                    },
                },
                headers=self._headers,
            )
            response.raise_for_status()
            return response.json()
