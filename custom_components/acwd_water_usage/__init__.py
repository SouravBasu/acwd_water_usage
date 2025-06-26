from .sensor import AcwdWaterUsage
from .const import DOMAIN

async def async_setup(hass, config):
    """Set up the ACWD Water Usage component."""
    return True
    
async def async_setup_entry(hass, config_entry):
    """Set up ACWD Water Usage from a config entry."""
    return await hass.config_entries.async_forward_entry_setups(config_entry, "sensor")

async def async_unload_entry(hass, config_entry):
    """Unload a config entry."""
    return await hass.config_entries.async_unload_platforms(config_entry, "sensor")

