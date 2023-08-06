name = "maloja"
desc = "Self-hosted music scrobble database"
author = {
	"name":"Johannes Krattenmacher",
	"email":"maloja@dev.krateng.ch",
	"github": "krateng"
}
version = 2,13,0
versionstr = ".".join(str(n) for n in version)
links = {
	"pypi":"malojaserver",
	"github":"maloja"
}
python_version = ">=3.6"
requires = [
	"bottle>=0.12.16",
	"waitress>=1.3",
	"doreah>=1.7.1",
	"nimrodel>=0.7.0",
	"setproctitle>=1.1.10",
	"wand>=0.5.4",
	"jinja2>=2.11",
	"lru-dict>=1.1.6",
	"css_html_js_minify>=2.5.5"
]
resources = [
	"web/*/*/*",
	"web/*/*",
	"web/*",
	"data_files/*/*",
	"data_files/*/*/*",
	"data_files/*/*/*/*",
	"*/*.py",
	"*/*/*.py",
	"*/*/*/*.py"
]

commands = {
	"maloja":"proccontrol.control:main"
}
