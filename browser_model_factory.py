#Embedded file name: /Users/versonator/Jenkins/live/output/mac_64_static/Release/midi-remote-scripts/Push/browser_model_factory.py
import Live
from .browser_model import filter_type_for_browser, EmptyBrowserModel, QueryingBrowserModel
from .browser_query import TagBrowserQuery, PathBrowserQuery, PlacesBrowserQuery, SourceBrowserQuery
FilterType = Live.Browser.FilterType
PLACES_LABEL = 'Places'

def make_plugins_query():
    return TagBrowserQuery(include=['Plug-ins'], root_name='plugins', subfolder='Plug-ins')


def make_midi_effect_browser_model(browser):
    midi_effects = TagBrowserQuery(include=['MIDI Effects'], root_name='midi_effects')
    max = TagBrowserQuery(include=[['Max for Live', 'Max MIDI Effect']], subfolder='Max for Live', root_name='max_for_live')
    plugins = make_plugins_query()
    places = PlacesBrowserQuery(subfolder=PLACES_LABEL)
    return QueryingBrowserModel(browser=browser, queries=[midi_effects,
     max,
     plugins,
     places])


def make_audio_effect_browser_model(browser):
    audio_effects = TagBrowserQuery(include=['Audio Effects'], root_name='audio_effects')
    max = TagBrowserQuery(include=[['Max for Live', 'Max Audio Effect']], subfolder='Max for Live', root_name='max_for_live')
    plugins = make_plugins_query()
    places = PlacesBrowserQuery(subfolder=PLACES_LABEL)
    return QueryingBrowserModel(browser=browser, queries=[audio_effects,
     max,
     plugins,
     places])


def make_instruments_browser_model(browser):
    instrument_rack = PathBrowserQuery(path=['Instruments', 'Instrument Rack'], root_name='instruments')
    drums = SourceBrowserQuery(include=['Drums'], exclude=['Drum Hits'], subfolder='Drum Rack', root_name='drums')
    instruments = TagBrowserQuery(include=['Instruments'], exclude=['Drum Rack', 'Instrument Rack'], root_name='instruments')
    drum_hits = TagBrowserQuery(include=[['Drums', 'Drum Hits']], subfolder='Drum Hits', root_name='drums')
    max = TagBrowserQuery(include=[['Max for Live', 'Max Instrument']], subfolder='Max for Live', root_name='max_for_live')
    plugins = make_plugins_query()
    places = PlacesBrowserQuery(subfolder=PLACES_LABEL)
    return QueryingBrowserModel(browser=browser, queries=[instrument_rack,
     drums,
     instruments,
     max,
     drum_hits,
     plugins,
     places])


def make_drum_pad_browser_model(browser):
    drums = TagBrowserQuery(include=[['Drums', 'Drum Hits']], root_name='drums')
    bell = SourceBrowserQuery(include=[['Drums', 'Drum Hits', 'Bell']], subfolder='Bell', root_name='drums')
    bongo = SourceBrowserQuery(include=[['Drums', 'Drum Hits', 'Bongo']], subfolder='Bongo', root_name='drums')
    clap = SourceBrowserQuery(include=[['Drums', 'Drum Hits', 'Clap']], subfolder='Clap', root_name='drums')
    conga = SourceBrowserQuery(include=[['Drums', 'Drum Hits', 'Conga']], subfolder='Conga', root_name='drums')
    cymbal = SourceBrowserQuery(include=[['Drums', 'Drum Hits', 'Cymbal']], subfolder='Cymbal', root_name='drums')
    fx_hit = SourceBrowserQuery(include=[['Drums', 'Drum Hits', 'FX Hit']], subfolder='FX Hit', root_name='drums')
    closedHihat = SourceBrowserQuery(include=[['Drums', 'Drum Hits', 'Closed Hihat']], subfolder='Closed Hihat', root_name='drums')
    openHihat = SourceBrowserQuery(include=[['Drums', 'Drum Hits', 'Open Hihat']], subfolder='Open Hihat', root_name='drums')
    kick = SourceBrowserQuery(include=[['Drums', 'Drum Hits', 'Kick']], subfolder='Kick', root_name='drums')
    misc = SourceBrowserQuery(include=[['Drums', 'Drum Hits', 'Misc Percussion']], subfolder='Misc Percussion', root_name='drums')
    ride = SourceBrowserQuery(include=[['Drums', 'Drum Hits', 'Ride']], subfolder='Ride', root_name='drums')
    rim = SourceBrowserQuery(include=[['Drums', 'Drum Hits', 'Rim']], subfolder='Rim', root_name='drums')
    shaker = SourceBrowserQuery(include=[['Drums', 'Drum Hits', 'Shaker']], subfolder='Shaker', root_name='drums')
    snare = SourceBrowserQuery(include=[['Drums', 'Drum Hits', 'Snare']], subfolder='Snare', root_name='drums')
    snare_art = SourceBrowserQuery(include=[['Drums', 'Drum Hits', 'Snare Articulation']], subfolder='Snare Articulation', root_name='drums')
    tambourine = SourceBrowserQuery(include=[['Drums', 'Drum Hits', 'Tambourine']], subfolder='Tambourine', root_name='drums')
    timbales = SourceBrowserQuery(include=[['Drums', 'Drum Hits', 'Timbales']], subfolder='Timbales', root_name='drums')
    tom = SourceBrowserQuery(include=[['Drums', 'Drum Hits', 'Tom']], subfolder='Tom', root_name='drums')
    wood = SourceBrowserQuery(include=[['Drums', 'Drum Hits', 'Wood']], subfolder='Wood', root_name='drums')
    samples = SourceBrowserQuery(include=['Samples'], subfolder='Samples', root_name='samples')
    instruments = TagBrowserQuery(include=['Instruments'], root_name='instruments')
    max = TagBrowserQuery(include=[['Max for Live', 'Max Instrument']], subfolder='Max for Live', root_name='max_for_live')
    plugins = make_plugins_query()
    places = PlacesBrowserQuery(subfolder=PLACES_LABEL)
    return QueryingBrowserModel(browser=browser, queries=[kick,
     snare, closedHihat, openHihat, clap, cymbal, ride, rim, shaker, tom, conga, tambourine, timbales, bell,
     wood, bongo, fx_hit, misc, snare_art,
     samples,
     instruments,
     max,
     plugins,
     places])


def make_fallback_browser_model(browser):
    return EmptyBrowserModel(browser=browser)


def make_browser_model(browser, filter_type = None):
    """
    Factory that returns an appropriate browser model depending on the
    browser filter type and hotswap target.
    """
    factories = {FilterType.instrument_hotswap: make_instruments_browser_model,
     FilterType.drum_pad_hotswap: make_drum_pad_browser_model,
     FilterType.audio_effect_hotswap: make_audio_effect_browser_model,
     FilterType.midi_effect_hotswap: make_midi_effect_browser_model}
    if filter_type == None:
        filter_type = filter_type_for_browser(browser)
    return factories.get(filter_type, make_fallback_browser_model)(browser)
