import winapps

apps = []
for app in winapps.list_installed():
    apps.append([app.name, app.version])

