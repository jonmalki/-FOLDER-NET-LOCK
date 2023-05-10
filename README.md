# -FOLDER-NET-LOCK
# Folder Net Lock

Folder Net Lock is a lightweight Python application that allows you to lock and unlock a folder on your Mac with a simple web interface. You can use this application to keep your files and folders private and secure, without the need for any third-party software.

## Features

- Simple and intuitive web interface
- Lock and unlock your folder with just one click
- Uses native `chflags` command to set/unset the "hidden" flag of the folder
- Works on macOS systems without any additional dependencies

## Installation

1. Clone or download the source code from the [GitHub repository](https://github.com/username/repo).
2. Install the required Python packages by running `pip install -r requirements.txt` in the terminal.
3. Create a folder named `f0ld3r` in the same directory as the application script. This will be the folder that you can lock and unlock.
4. Run the application by running `python app.py` in the terminal.

## Usage

Once the application is running, you can access the web interface by opening a web browser and navigating to `http://localhost:5001`. You should see a page with two buttons: "Lock" and "Unlock". Clicking on these buttons will toggle the visibility of the `f0ld3r` folder in the Finder.

## Customization

You can customize the appearance of the web page by editing the HTML and CSS code in the `app.py` file. You can also change the name and location of the folder to be locked by modifying the `subprocess.run` commands in the `lock_folder` and `unlock_folder` functions.

## Contributing

If you want to contribute to the development of Folder Net Lock, feel free to submit a pull request or open an issue on the [GitHub repository](https://github.com/username/repo). Any feedback or suggestions are also welcome.

## License

Folder Net Lock is released under the [MIT License](https://opensource.org/licenses/MIT). You can use, modify, and distribute the code as you like, as long as you include the original license and disclaimer. However, please note that the application is provided "as is" and without warranty of any kind. Use at your own risk.
