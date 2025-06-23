import httpx


class SmartConsoleAdapter:
    def __init__(self, base_url: str, api_key: str):
        self.base_url = base_url
        self.api_key = api_key

    def _get_headers(self):
        return {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json",
        }

    async def get_resource(self, resource_id: str):
        url = f"{self.base_url}/resources/{resource_id}"
        async with httpx.AsyncClient() as client:
            response = await client.get(url, headers=self._get_headers())
            response.raise_for_status()
            return response.json()

    async def create_resource(self, resource_data: dict):
        url = f"{self.base_url}/resources"
        async with httpx.AsyncClient() as client:
            response = await client.post(
                url, json=resource_data, headers=self._get_headers()
            )
            response.raise_for_status()
            return response.json()

    async def update_resource(self, resource_id: str, resource_data: dict):
        url = f"{self.base_url}/resources/{resource_id}"
        async with httpx.AsyncClient() as client:
            response = await client.put(
                url, json=resource_data, headers=self._get_headers()
            )
            response.raise_for_status()
            return response.json()

    async def delete_resource(self, resource_id: str):
        url = f"{self.base_url}/resources/{resource_id}"
        async with httpx.AsyncClient() as client:
            response = await client.delete(url, headers=self._get_headers())
            response.raise_for_status()
            return response.status_code == 204
