#
# Gramps - a GTK+/GNOME based genealogy program
#
# Copyright (C) 2004-2007  Donald N. Allingham
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, 
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA
#

# $Id$

"""
Class handling language-specific selection for date parser and displayer.
"""

#-------------------------------------------------------------------------
#
# set up logging
#
#-------------------------------------------------------------------------
import logging

from ..const import GRAMPS_LOCALE as glocale
_ = glocale.translation.sgettext
# import prerequisites for localized handlers
from ._datehandler import (LANG, LANG_SHORT, LANG_TO_PARSER, LANG_TO_DISPLAY, 
                          register_datehandler)

# Import all the localized handlers
from . import _date_bg
from . import _date_ca
from . import _date_cs
from . import _date_da
from . import _date_de
from . import _date_el
from . import _date_es
from . import _date_fi
from . import _date_fr
from . import _date_hr
from . import _date_it
from . import _date_lt
from . import _date_nb
from . import _date_nl
from . import _date_pl
from . import _date_pt
from . import _date_ru
from . import _date_sk
from . import _date_sl
from . import _date_sr
from . import _date_sv
from . import _date_uk

# Initialize global parser
try:
    if LANG in LANG_TO_PARSER:
        parser = LANG_TO_PARSER[LANG]()
    else:
        parser = LANG_TO_PARSER[LANG_SHORT]()
except:
    logging.warning(_("Date parser for '%s' not available, using default") % LANG)
    parser = LANG_TO_PARSER["C"]()

# Initialize global displayer
try:
    from ..config import config
    val = config.get('preferences.date-format')
except:
    val = 0

try:
    if LANG in LANG_TO_DISPLAY:
        displayer = LANG_TO_DISPLAY[LANG](val)
    else:
        displayer = LANG_TO_DISPLAY[LANG_SHORT](val)
except:
    logging.warning(_("Date displayer for '%s' not available, using default") % LANG)
    displayer = LANG_TO_DISPLAY["C"](val)


# Import utility functions
from ._dateutils import *
from ._grampslocale import (codeset, month_to_int, long_months, short_months, 
                           long_days, short_days, tformat)