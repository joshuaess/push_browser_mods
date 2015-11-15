#!/usr/bin/env bash
#
#installs my browser mods
#

if ! ( groups | grep -i 'admin' ); then
  echo 'you must run this script from an administrator account'
  exit 1
fi

PS3="Please select an installation of Ableton 9.5 or higher : "
select ABLETON_APP in /Applications/Ableton* quit; do
  ABLETON_MINOR_VERSION="$(mdls -name kMDItemVersion "$ABLETON_APP" | cut -d'.' -f2 )"
if [[ "$ABLETON_APP" == "quit" ]]; then
  break
fi
  if [[ "$ABLETON_MINOR_VERSION" -ge 5 ]]; then
    echo 'Version 9.5 or higher detected'
    if [[ -d "${ABLETON_APP}/Contents/App-Resources/MIDI Remote Scripts/Push_Mod" ]]; then
      echo "Push_Mod folder already exists...Please copy these files manually into ${ABLETON_APP}/Contents/App-Resources/MIDI Remote Scripts/Push_Mod"
      exit 1
    else
      SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
      echo 'Creating Push_Mod folder...'
      cp -R "${ABLETON_APP}/Contents/App-Resources/MIDI Remote Scripts/Push" "${ABLETON_APP}/Contents/App-Resources/MIDI Remote Scripts/Push_Mod"
      cp "${SCRIPT_DIR}"/*.py "${ABLETON_APP}/Contents/App-Resources/MIDI Remote Scripts/Push_Mod"
      exit 0
    fi
  fi
done
