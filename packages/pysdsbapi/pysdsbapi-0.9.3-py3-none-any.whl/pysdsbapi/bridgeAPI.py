from typing import List
from .auth import Auth
from .module import Module
from .bridge import Bridge


class BridgeAPI:

    def __init__(self, auth: Auth):        
        """Initialize the API and store the auth so we can make requests."""        
        self.auth = auth

    async def async_is_valid_login(self) -> bool:
        # Use get bridge to check if login works
        # ToDo: Test if this works
        try:
            await self.async_get_bridge(self)
            return True
        except:
            return False

    async def async_get_modules(self) -> List[Module]:
        response = await self.auth.request("get", "modules/show")
        response.raise_for_status()
        return [Module(module_data, self.auth) for module_data in await response.json()]

    async def async_get_module(self, moduleId: str) -> List[Module]:
        response = await self.auth.request("get", f"modules/show?id={moduleId}")
        response.raise_for_status()
        #ToDo: Should return not a list
        #return Module(await response.json(), self.auth)
        return[Module(module_data, self.auth) for module_data in await response.json()]

    async def async_get_bridge(self) -> Bridge:
        response = await self.auth.request("get", "check")
        response.raise_for_status()
        return Bridge(await response.json(), self.auth)