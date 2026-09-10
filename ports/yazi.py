from ports._cli import row
from ports._lib import HEADER, Out, ink, selection
from ports.bat import tmtheme

META = {
    "id": "yazi",
    "name": "Yazi",
    "category": "CLI & TUI",
    "homepage": "https://yazi-rs.github.io",
    "enable": {
        "where": "~/.config/yazi/theme.toml",
        "code": '[flavor]\ndark  = "{slug}"\nlight = "{slug}"',
        "lang": "toml",
    },
    "auto": {
        "where": "~/.config/yazi/theme.toml (Yazi picks by the terminal's background)",
        "code": '[flavor]\ndark  = "subway-seat"\nlight = "subway-seat-enamel"',
        "lang": "toml",
    },
    "requires": "Yazi 25.2+",
    "detect": ["yazi"],
    "notes": "Yazi flavors with gold directories, an orange mode badge and a gold bar on the hovered "
    "file; previews use the bundled tmTheme, and Yazi's file icons are recolored in the palette.",
}


def style(fg=None, bg=None, **attrs):
    parts = [f'fg = "{fg}"'] if fg else []
    parts += [f'bg = "{bg}"'] if bg else []
    parts += [f"{k} = true" for k, v in attrs.items() if v]
    return "{ " + ", ".join(parts) + " }" if parts else "{}"


def flavor(f):
    on, sel = ink(f), selection(f)
    accent = style(f.orange)
    sections = {
        "app": {"overall": style(bg=f.base)},
        "mgr": {
            "cwd": style(f.yellow),
            "find_keyword": style(f.yellow, bold=True, italic=True, underline=True),
            "find_position": f'{{ fg = "{f.orange}", bg = "reset", bold = true, italic = true }}',
            "symlink_target": style(f.sage, italic=True),
            "marker_copied": style(f.green, f.green),
            "marker_cut": style(f.red_hi, f.red_hi),
            "marker_marked": style(f.sage, f.sage),
            "marker_selected": style(f.yellow, f.yellow),
            "count_copied": style(on, f.green),
            "count_cut": style(on, f.red_hi),
            "count_selected": style(on, f.yellow),
            "border_style": style(f.surface2),
        },
        "tabs": {
            "active": style(on, f.orange, bold=True),
            "inactive": style(f.subtext1, f.surface1),
        },
        "mode": {
            "normal_main": style(on, f.orange, bold=True),
            "normal_alt": style(f.orange, f.surface0),
            "select_main": style(on, f.green, bold=True),
            "select_alt": style(f.green, f.surface0),
            "unset_main": style(on, f.red_hi, bold=True),
            "unset_alt": style(f.red_hi, f.surface0),
        },
        "indicator": {
            "parent": style(f.text_hi, f.surface1),
            "current": style(on, f.yellow),
            "preview": style(f.text_hi, f.surface1),
        },
        "status": {
            "perm_sep": style(f.overlay0),
            "perm_type": style(f.sage),
            "perm_read": style(f.yellow),
            "perm_write": style(f.orange),
            "perm_exec": style(f.green),
            "progress_label": style(f.text_hi, bold=True),
            "progress_normal": style(f.green, f.surface1),
            "progress_error": style(f.red_hi, f.surface1),
        },
        "which": {
            "border": accent,
            "mask": style(bg=f.mantle),
            "cand": style(f.yellow),
            "rest": style(f.overlay1),
            "desc": style(f.subtext1),
            "separator_style": style(f.surface2),
        },
        "confirm": {
            "border": accent,
            "title": style(f.orange, bold=True),
            "body": "{}",
            "list": "{}",
            "btn_yes": style(on, f.orange, bold=True),
            "btn_no": style(f.subtext1),
        },
        "spot": {
            "border": accent,
            "title": accent,
            "tbl_col": style(f.sage),
            "tbl_cell": style(on, f.yellow),
        },
        "notify": {
            "title_info": style(f.denim),
            "title_warn": style(f.yellow),
            "title_error": style(f.red_hi),
        },
        "pick": {"border": accent, "active": style(f.orange, bold=True), "inactive": "{}"},
        "input": {"border": accent, "title": "{}", "value": "{}", "selected": style(f.text_hi, sel)},
        "cmp": {"border": accent, "active": style(f.text_hi, row(f)), "inactive": "{}"},
        "tasks": {"border": accent, "title": "{}", "hovered": style(f.orange, bold=True)},
        "help": {
            "border": accent,
            "chord": style(f.yellow),
            "action": style(f.subtext1),
            "hovered": style(bg=row(f), bold=True),
        },
    }
    out = [f"# {HEADER}", f"# {f.name} flavor for Yazi.", ""]
    for name, keys in sections.items():
        out.append(f"[{name}]")
        width = max(map(len, keys))
        out += [f"{k:<{width}} = {v}" for k, v in keys.items()]
        out.append("")

    rules = [
        "# Media",
        f'{{ mime = "**/image/*", fg = "{f.clay}" }}',
        f'{{ mime = "**/{{audio,video}}/*", fg = "{f.orange}" }}',
        "# Archives",
        (
            '{ mime = "**/application/{zip,rar,7z*,tar,gzip,xz,zstd,bzip*,lzma,compress,archive,cpio,arj,xar,ms-cab*}", '
            f'fg = "{f.red_hi}" }}'
        ),
        "# Documents",
        f'{{ mime = "**/application/{{pdf,doc,rtf}}", fg = "{f.denim}" }}',
        "# Virtual file system",
        f'{{ mime = "vfs/{{absent,stale}}", fg = "{f.overlay0}" }}',
        "# Special files",
        f'{{ url = "*", is = "orphan", fg = "{on}", bg = "{f.red}" }}',
        f'{{ url = "*", is = "exec", fg = "{f.green}" }}',
        "# Dummy files",
        f'{{ url = "*", is = "dummy", fg = "{on}", bg = "{f.red}" }}',
        f'{{ url = "*/", is = "dummy", fg = "{on}", bg = "{f.red}" }}',
        "# Fallback",
        f'{{ url = "*/", fg = "{f.yellow}", bold = true }}',
    ]
    out.append("[filetype]\nrules = [")
    out += [f"\t{r}" + ("" if r.startswith("#") else ",") for r in rules]
    out += ["]", ""]

    dirs = [
        (".config", "\ue5fc"), (".git", "\ue5fb"), (".github", "\ue5fd"), (".npm", "\ue5fa"),
        ("Desktop", "\uf108"), ("Development", "\ue70c"), ("Documents", "\uf401"), ("Downloads", "\uf498"),
        ("Library", "\ueb9c"), ("Movies", "\uf447"), ("Music", "\uf025"), ("Pictures", "\ue244"),
        ("Public", "\uf42b"), ("Videos", "\uf447"),
    ]
    conds = [
        ("orphan", "\uf127", f.red_hi), ("link", "\uf481", f.sage),
        ("block", "\uf0c9", f.clay), ("char", "\uf1c0", f.clay), ("fifo", "\uf1d1", f.clay),
        ("sock", "\uf1e4", f.clay), ("sticky", "\uf08d", f.clay), ("dummy", "\uf057", f.red_hi),
        ("dir & hovered", "\ue5fe", f.yellow), ("dir", "\ue5ff", f.yellow),
        ("exec", "\uf489", f.green), ("!dir", "\uf15b", f.subtext1),
    ]
    out.append("[icon]\ndirs = [")
    out += [f'\t{{ name = "{n}", text = "{g}", fg = "{f.yellow}" }},' for n, g in dirs]
    out.append("]\nconds = [")
    out += [f'\t{{ if = "{c}", text = "{g}", fg = "{col}" }},' for c, g, col in conds]
    for line in ICONS.splitlines():
        if line.startswith("["):
            out += ["]", f"prepend_{line[1:-1]} = ["]
        else:
            name, glyph, role = line.split(" ")
            out.append(f'\t{{ name = "{name}", text = "{glyph}", fg = "{f.colors[role]}" }},')
    out += ["]", ""]
    return "\n".join(out)


def build(flavors):
    outs = []
    for f in flavors:
        base = f"~/.config/yazi/flavors/{f.slug}.yazi"
        outs.append(Out(f"{f.slug}.yazi/flavor.toml", flavor(f), flavor=f.id, dest=f"{base}/flavor.toml", lang="toml"))
        outs.append(Out(f"{f.slug}.yazi/tmtheme.xml", tmtheme(f), flavor=f.id, dest=f"{base}/tmtheme.xml", lang="xml"))
    return outs


# Yazi's own file and extension icons (MIT; yazi-config/preset/theme-dark.toml, 26.9),
# each Material color mapped by hue to the nearest palette role. The flavor writes
# them as prepend_files/prepend_exts, so icons Yazi adds later still show.
ICONS = """\
[files]
.babelrc  yellow
.bash_profile  green
.bashrc  green
.clang-format  overlay2
.clang-tidy  overlay2
.codespellrc 󰓆 green
.condarc  green
.dockerignore 󰡨 denim
.ds_store  overlay2
.editorconfig  subtext1
.env  yellow
.eslintignore  denim
.eslintrc  denim
.git-blame-ignore-revs  orange
.gitattributes  orange
.gitconfig  orange
.gitignore  orange
.gitlab-ci.yml  orange
.gitmodules  orange
.gtkrc-2.0  subtext1
.gvimrc  green
.justfile  overlay2
.luacheckrc  denim
.luaurc  denim
.mailmap 󰊢 orange
.nanorc  clay
.npmignore  red_hi
.npmrc  red_hi
.nuxtrc 󱄆 sage
.nvmrc  green
.pnpmfile.cjs  yellow
.pre-commit-config.yaml 󰛢 yellow
.prettierignore  denim
.prettierrc  denim
.prettierrc.cjs  denim
.prettierrc.js  denim
.prettierrc.json  denim
.prettierrc.json5  denim
.prettierrc.mjs  denim
.prettierrc.toml  denim
.prettierrc.yaml  denim
.prettierrc.yml  denim
.pylintrc  overlay2
.settings.json  clay
.SRCINFO 󰣇 sage
.vimrc  green
.Xauthority  orange
.xinitrc  orange
.Xresources  orange
.xsession  orange
.zprofile  green
.zshenv  green
.zshrc  green
_gvimrc  green
_vimrc  green
AUTHORS  clay
AUTHORS.txt  clay
brewfile  orange
bspwmrc  overlay2
build  green
build.gradle  sage
build.zig.zon  yellow
bun.lock  subtext1
bun.lockb  subtext1
cantorrc  denim
checkhealth 󰓙 denim
cmakelists.txt  subtext1
code_of_conduct  red_hi
code_of_conduct.md  red_hi
commit_editmsg  orange
commitlint.config.js 󰜘 sage
commitlint.config.ts 󰜘 sage
compose.yaml 󰡨 denim
compose.yml 󰡨 denim
config  overlay2
containerfile 󰡨 denim
copying  yellow
copying.lesser  yellow
Directory.Build.props  denim
Directory.Build.targets  denim
Directory.Packages.props  denim
docker-compose.yaml 󰡨 denim
docker-compose.yml 󰡨 denim
dockerfile 󰡨 denim
eslint.config.cjs  denim
eslint.config.js  denim
eslint.config.mjs  denim
eslint.config.ts  denim
ext_typoscript_setup.txt  clay
favicon.ico  yellow
fp-info-cache  subtext1
fp-lib-table  subtext1
FreeCAD.conf  orange
Gemfile  orange
gnumakefile  overlay2
go.mod  sage
go.sum  sage
go.work  sage
gradle-wrapper.properties  sage
gradle.properties  sage
gradlew  sage
groovy  sage
gruntfile.babel.js  clay
gruntfile.coffee  clay
gruntfile.js  clay
gruntfile.ts  clay
gtkrc  subtext1
gulpfile.babel.js  orange
gulpfile.coffee  orange
gulpfile.js  orange
gulpfile.ts  orange
hypridle.conf  sage
hyprland.conf  sage
hyprlandd.conf  sage
hyprlock.conf  sage
hyprpaper.conf  sage
hyprsunset.conf  sage
i18n.config.js 󰗊 denim
i18n.config.ts 󰗊 denim
i3blocks.conf  subtext1
i3status.conf  subtext1
index.theme  sage
ionic.config.json  denim
Jenkinsfile  orange
justfile  overlay2
kalgebrarc  denim
kdeglobals  denim
kdenlive-layoutsrc  denim
kdenliverc  denim
kritadisplayrc  clay
kritarc  clay
license  yellow
license.md  yellow
lxde-rc.xml  overlay2
lxqt.conf  sage
makefile  overlay2
mix.lock  clay
mpv.conf  clay
next.config.cjs  subtext1
next.config.js  subtext1
next.config.ts  subtext1
node_modules  red_hi
nuxt.config.cjs 󱄆 sage
nuxt.config.js 󱄆 sage
nuxt.config.mjs 󱄆 sage
nuxt.config.ts 󱄆 sage
package-lock.json  red_hi
package.json  red_hi
PKGBUILD  sage
platformio.ini  clay
playwright.config.cjs  green
playwright.config.cts  green
playwright.config.js  green
playwright.config.mjs  green
playwright.config.mts  green
playwright.config.ts  green
pnpm-lock.yaml  yellow
pnpm-workspace.yaml  yellow
pom.xml  red_hi
prettier.config.cjs  denim
prettier.config.js  denim
prettier.config.mjs  denim
prettier.config.ts  denim
prisma.config.mts  denim
prisma.config.ts  denim
procfile  clay
PrusaSlicer.ini  orange
PrusaSlicerGcodeViewer.ini  orange
py.typed  yellow
QtProject.conf  green
rakefile  orange
readme 󰂺 subtext1
readme.md 󰂺 subtext1
rmd  sage
robots.txt 󰚩 denim
security 󰒃 subtext1
security.md 󰒃 subtext1
settings.gradle  sage
svelte.config.js  orange
sxhkdrc  overlay2
sym-lib-table  subtext1
tailwind.config.js 󱏿 sage
tailwind.config.mjs 󱏿 sage
tailwind.config.ts 󱏿 sage
tmux.conf  green
tmux.conf.local  green
tsconfig.json  sage
unlicense  yellow
vagrantfile  denim
vercel.json  subtext1
vite.config.cjs  yellow
vite.config.cts  yellow
vite.config.js  yellow
vite.config.mjs  yellow
vite.config.mts  yellow
vite.config.ts  yellow
vitest.config.cjs  green
vitest.config.cts  green
vitest.config.js  green
vitest.config.mjs  green
vitest.config.mts  green
vitest.config.ts  green
vlcrc 󰕼 clay
webpack 󰜫 sage
weston.ini  yellow
workspace  green
wrangler.jsonc  clay
wrangler.toml  clay
xdph.conf  sage
xmobarrc  red_hi
xmobarrc.hs  red_hi
xmonad.hs  red_hi
xorg.conf  orange
xsettingsd.conf  orange
[exts]
3gp  clay
3mf 󰆧 overlay2
7z  yellow
a  subtext1
aac  sage
ada  denim
adb  denim
ads  clay
ai  yellow
aif  sage
aiff  sage
android  green
ape  sage
apk  green
apl  green
app  orange
applescript  overlay2
asc 󰦝 overlay2
asm  sage
ass 󰨖 yellow
astro  red_hi
avif  clay
awk  overlay2
azcli  denim
bak 󰁯 overlay2
bash  green
bat  green
bazel  green
bib 󱉟 yellow
bicep  sage
bicepparam  clay
bin  orange
blade.php  orange
blend 󰂫 clay
blp 󰺾 denim
bmp  clay
bqn  green
brep 󰻫 green
bz  yellow
bz2  yellow
bz3  yellow
bzl  green
c  denim
c++  red_hi
cache  subtext1
cast  clay
cbl  denim
cc  red_hi
ccm  red_hi
cfc  sage
cfg  overlay2
cfm  sage
cjs  yellow
clj  green
cljc  green
cljd  sage
cljs  sage
cmake  subtext1
cob  denim
cobol  denim
coffee  yellow
conda  green
conf  overlay2
config.ru  orange
cow 󰆚 clay
cp  sage
cpp  sage
cppm  sage
cpy  denim
cr  subtext1
crdownload  sage
cs 󰌛 green
csh  overlay2
cshtml 󱦗 denim
cson  yellow
csproj 󰪮 denim
css  clay
csv  green
cts  sage
cu  green
cue 󰲹 red_hi
cuh  clay
cxx  sage
cxxm  sage
d  orange
d.ts  yellow
dart  denim
db  subtext1
dconf  subtext1
desktop  clay
diff  overlay2
dll  clay
doc 󰈬 denim
Dockerfile 󰡨 denim
dockerignore 󰡨 denim
docx 󰈬 denim
dot 󱁉 denim
download  sage
drl  red_hi
dropbox  denim
dump  subtext1
dwg 󰻫 green
dxf 󰻫 green
ebook  yellow
ebuild  clay
edn  sage
eex  clay
ejs  yellow
el  clay
elc  clay
elf  orange
elm  sage
eln  clay
env  yellow
eot  subtext1
epp  yellow
epub  yellow
erb  orange
erl  clay
ex  clay
exe  orange
exs  clay
f#  sage
f3d 󰻫 green
f90 󱈚 clay
fbx 󰆧 overlay2
fcbak  orange
fcmacro  orange
fcmat  orange
fcparam  orange
fcscript  orange
fcstd  orange
fcstd1  orange
fctb  orange
fctl  orange
fdmdownload  sage
feature  green
fish  overlay2
flac  sage
flc  subtext1
flf  subtext1
fnl  subtext1
fodg  yellow
fodp  clay
fods  green
fodt  sage
frag  sage
fs  sage
fsi  sage
fsscript  sage
fsx  sage
gcode 󰐫 sage
gd  overlay2
gemspec  orange
geom  sage
gif  clay
git  orange
glb  yellow
gleam  clay
glsl  sage
gnumakefile  overlay2
go  sage
godot  overlay2
gpr  overlay2
gql  red_hi
gradle  sage
graphql  red_hi
gresource  subtext1
gv 󱁉 denim
gz  yellow
h  clay
haml  subtext1
hbs  orange
heex  clay
hex  denim
hh  clay
hpp  clay
hrl  clay
hs  clay
htm  orange
html  orange
http  sage
huff 󰡘 denim
hurl  red_hi
hx  clay
hxx  clay
ical  denim
icalendar  denim
ico  yellow
ics  denim
ifb  denim
ifc 󰻫 green
ige 󰻫 green
iges 󰻫 green
igs 󰻫 green
image  subtext1
img  subtext1
import  subtext1
info  yellow
ini  overlay2
ino  sage
ipynb  clay
iso  subtext1
ixx  sage
jar  clay
java  orange
jl  clay
jpeg  clay
jpg  clay
js  yellow
json  yellow
json5  yellow
jsonc  yellow
jsx  sage
jwmrc  denim
jxl  clay
kbx 󰯄 overlay2
kdb  green
kdbx  green
kdenlive  denim
kdenlivetitle  denim
kicad_dru  subtext1
kicad_mod  subtext1
kicad_pcb  subtext1
kicad_prl  subtext1
kicad_pro  subtext1
kicad_sch  subtext1
kicad_sym  subtext1
kicad_wks  subtext1
ko  subtext1
kpp  clay
kra  clay
krz  clay
ksh  overlay2
kt  denim
kts  denim
lck  subtext1
leex  clay
less  clay
lff  subtext1
lhs  clay
lib  clay
license  yellow
liquid  green
lock  subtext1
log 󰌱 subtext1
lrc 󰨖 yellow
lua  sage
luac  sage
luau  denim
m  denim
m3u 󰲹 red_hi
m3u8 󰲹 red_hi
m4a  sage
m4v  clay
magnet  orange
makefile  overlay2
markdown  subtext1
material  clay
md  subtext1
md5 󰕥 clay
mdx  sage
mint 󰌪 sage
mjs  yellow
mk  overlay2
mkv  clay
ml  clay
mli  clay
mm  sage
mo  clay
mobi  yellow
mojo  orange
mov  clay
mp3  sage
mp4  clay
mpp  sage
msf  denim
mts  sage
mustache  clay
nfo  yellow
nim  yellow
nix  sage
norg  denim
nswag  green
nu  sage
o  orange
obj 󰆧 overlay2
odf  red_hi
odg  yellow
odin 󰟢 denim
odp  clay
ods  green
odt  sage
oga  sage
ogg  sage
ogv  clay
ogx  clay
opus  sage
org  sage
otf  subtext1
out  orange
part  sage
patch  overlay2
pck  overlay2
pcm  sage
pdf  orange
php  clay
pl  sage
pls 󰲹 red_hi
ply 󰆧 overlay2
pm  sage
png  clay
po  sage
pot  sage
pp  yellow
ppt 󰈧 orange
pptx 󰈧 orange
prisma  denim
pro  yellow
ps1 󰨊 denim
psb  sage
psd  sage
psd1 󰨊 denim
psm1 󰨊 denim
pub 󰷖 yellow
pxd  sage
pxi  sage
py  yellow
pyc  yellow
pyd  yellow
pyi  yellow
pyo  yellow
pyw  sage
pyx  sage
qm  sage
qml  green
qrc  green
qss  green
query  green
R 󰟔 denim
r 󰟔 denim
rake  orange
rar  yellow
rasi  yellow
razor 󱦘 denim
rb  orange
res  orange
resi  red_hi
rlib  clay
rmd  sage
rproj 󰗆 sage
rs  clay
rss  clay
s  denim
sass  red_hi
sbt  orange
sc  orange
scad  yellow
scala  orange
scm 󰘧 subtext1
scss  red_hi
sh  overlay2
sha1 󰕥 clay
sha224 󰕥 clay
sha256 󰕥 clay
sha384 󰕥 clay
sha512 󰕥 clay
sig 󰘧 clay
signature 󰘧 clay
skp 󰻫 green
sldasm 󰻫 green
sldprt 󰻫 green
slim  orange
sln  clay
slnx  clay
slvs 󰻫 green
sml 󰘧 clay
so  subtext1
sol  sage
spec.js  yellow
spec.jsx  sage
spec.ts  sage
spec.tsx  denim
spx  sage
sql  subtext1
sqlite  subtext1
sqlite3  subtext1
srt 󰨖 yellow
ssa 󰨖 yellow
ste 󰻫 green
step 󰻫 green
stl 󰆧 overlay2
stories.js  red_hi
stories.jsx  red_hi
stories.mjs  red_hi
stories.svelte  red_hi
stories.ts  red_hi
stories.tsx  red_hi
stories.vue  red_hi
stp 󰻫 green
strings  sage
styl  green
sub 󰨖 yellow
sublime  clay
suo  clay
sv 󰍛 green
svelte  orange
svg 󰜡 yellow
svgz 󰜡 yellow
svh 󰍛 green
swift  clay
t  sage
tbc 󰛓 denim
tcl 󰛓 denim
templ  yellow
terminal  green
test.js  yellow
test.jsx  sage
test.ts  sage
test.tsx  denim
tex  green
tf  denim
tfvars  denim
tgz  yellow
tmpl  yellow
tmux  green
toml  orange
torrent  sage
tres  overlay2
ts  sage
tscn  overlay2
tsconfig  clay
tsx  denim
ttf  subtext1
twig  green
txt 󰈙 green
txz  yellow
typ  sage
typoscript  clay
ui  denim
v 󰍛 green
vala  clay
vert  sage
vh 󰍛 green
vhd 󰍛 green
vhdl 󰍛 green
vi  yellow
vim  green
vsh  denim
vsix  clay
vue  green
wasm  denim
wav  sage
webm  clay
webmanifest  yellow
webp  clay
webpack 󰜫 sage
wma  sage
wmv  clay
woff  subtext1
woff2  subtext1
wrl 󰆧 overlay2
wrz 󰆧 overlay2
wv  sage
wvc  sage
x  denim
xaml 󰙳 denim
xcf  overlay2
xcplayground  clay
xcstrings  sage
xls 󰈛 sage
xlsx 󰈛 sage
xm  sage
xml 󰗀 clay
xpi  orange
xslt 󰗀 sage
xul  clay
xz  yellow
yaml  overlay2
yml  overlay2
zig  yellow
zip  yellow
zsh  green
zst  yellow
🔥  orange
"""
