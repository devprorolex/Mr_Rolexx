from NOVA_MUSIC.core.bot import NOVA_MUSICBot
from NOVA_MUSIC.core.dir import dirr
from NOVA_MUSIC.core.git import git
from NOVA_MUSIC.core.userbot import Userbot
from NOVA_MUSIC.misc import dbb, heroku, sudo

from .logging import LOGGER


dirr()

git()

dbb()

heroku()

sudo()

# Clients
app = NOVAXBot()
userbot = Userbot()


from .platforms import *

YouTube = YouTubeAPI()
Carbon = CarbonAPI()
Spotify = SpotifyAPI()
Apple = AppleAPI()
Resso = RessoAPI()
SoundCloud = SoundAPI()
Telegram = TeleAPI()
