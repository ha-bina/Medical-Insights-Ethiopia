CHANNEL_REGISTRY = {
    'chemed': 'ChemedEthiopia',
    'lobelia': 'lobelia4cosmetics',
    'tikvah': 'tikvahpharma',
    # Add more channels from et.tgstat.com/medicine
}

def get_channel_handle(short_name):
    """Get full channel handle from registry"""
    return CHANNEL_REGISTRY.get(short_name)