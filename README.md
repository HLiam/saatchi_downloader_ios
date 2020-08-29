saatchi_downloader_ios is a tool to enable downloading from saatchi.com on your
iOS device using the (paid) [Pythonista app][1].

&nbsp;

# Installing
1. Download the repository onto your iOS device. If you have a (third-party)
git framework installed for the app, this will be easy. If not, you'll
likely have to do it in a hacky way, like putting it on Google Drive and
downloading it onto your device from there.
2. Create the share shortcut:
    1. Open the `saatchi_downloader.py` script on your device.
    2. Tap the wrench icon in the top-right.
    3. Tap the button that says 'Shortcuts' (the icon is an arrow pointing up
           and to the right).
    4. Tap the list item that says 'Share Extension'.
    5. Tap the add-new icon (end of the list; the icon is a plus symbol in a
           circle).
    6. Set the settings at follows (or customize however you see fit):
        - Reset Environment: on
        - Custom Title: 'Saatchi Download'
        - Icon: 'load-c' (it kinda looks like the Saatchi logo)
        - Icon Color: #dc3a0f (used in Saatchi's color pallet)
    7. Tap the 'Add' button in the top-right.

# Using
saatchi_downloader can be used in four ways:
1. Sharing the url of a saatchi artwork page from the share button (select 'Run
Pythonista Script', then select the script).
2. Passing the artwork page url as the first system argument to the script.
3. From the chipboard, if it contains an eligible url (valid url formatting and
points to a saatchi.com artwork page).
4. Asking the user to type it via the console.

[1]: https://apps.apple.com/ca/app/pythonista-3/id1085978097
