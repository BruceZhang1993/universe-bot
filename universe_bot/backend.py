import pkg_resources

available_backends = {
    entry_point.name: entry_point.load()
    for entry_point in pkg_resources.iter_entry_points('universe_bot.backend')
}
