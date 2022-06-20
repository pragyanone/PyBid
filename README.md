
# PyBid
Prepare [Bolpatra (PPMO)](https://www.bolpatra.gov.np/egp/) bid documents of 'Works' category.

## Installation
Download the executable from the [Releases Page](https://github.com/pragyanone/PyBid/releases).

Or, `pip install PyBid`.

*If you are on windows and don't have `lxml` (dependency of python-docx), download the appropriate [lxml.whl](https://www.lfd.uci.edu/~gohlke/pythonlibs/#lxml) file and use `pip` to install it.*

[Install on Android *(useful for tablets)*](#install-on-android)

## Usage
```
python -m PyBid.PyBid
```

Then provide the details of the contract.
Documents will be created in the *'SOURCE'* sub-directory of the corresponding *project* directory.

## Install on Android
1. Install [Termux](https://f-droid.org/en/packages/com.termux)
2. `pkg install python python-tkinter libxml2 libxslt libiconv clang`
3. `pip install wheel`
4. `pip install lxml PyBid`
5. Install and setup a [Graphical Environment](https://wiki.termux.com/wiki/Graphical_Environment). Use [VNC Viewer - Remote Desktop](https://play.google.com/store/apps/details?id=com.realvnc.viewer.android) as the client.
6. Create an alias *(shortcut)* for PyBid as `PyBid`. Make sure 'Documents' folder exists in your Internal Storage.
```
termux-setup-storage
echo "
alias PyBid='
cd /data/data/com.termux/files/home/storage/shared/Documents;
export DISPLAY=\":1\";
echo \"Launching PyBid in vnc-server...\";
echo \"Select Termux in vnc-viewer\";
sleep 3;
am start --user 0 com.realvnc.viewer.android/com.realvnc.viewer.android.app.ConnectionChooserActivity >/dev/null;
python -m PyBid.PyBid'
" >> ../usr/etc/bash.bashrc
```
7. Restart Termux
8. `PyBid`

Video Tutorial:

[![PyBid on Android](https://github.com/pragyanone/PyBid/blob/master/blob/Thumbnail.png)](https://www.youtube.com/watch?v=CQXYXuep1N4 "PyBid Installation on Android")
