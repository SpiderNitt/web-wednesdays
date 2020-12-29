const { app, BrowserWindow, Menu, ipcMain } = require("electron");
process.env.NODE_ENV = "development";
let mainWindow, addWindow;

//Dotenv config
if (process.env.NODE_ENV !== "production") {
  require("dotenv").config();
}

//Main window
const createMainWindow = () => {
  mainWindow = new BrowserWindow({
    width: 800,
    height: 600,
    webPreferences: {
      nodeIntegration: true,  //Grants access to use NodeJS API
    },
  });
  mainWindow.loadFile("index.html");

  //Quits the app on closing the main window
  mainWindow.on("closed", () => {
    app.quit();
  });

  //Builds custom menu from a template
  const mainMenu = Menu.buildFromTemplate(mainMenuTemplate);
  Menu.setApplicationMenu(mainMenu);
};

//Additional window
const createAddWindow = () => {
  addWindow = new BrowserWindow({
    width: 350,
    height: 250,
    webPreferences: {
      nodeIntegration: true,
    },
  });
  addWindow.loadFile("add.html");

  addWindow.on("close", () => {
    addWindow = null;
  });
};

//Loads the main window
app.whenReady().then(createMainWindow);

//Receives data from addWindow and sends it to mainWindow
ipcMain.on("city:find", (e, city) => {
  mainWindow.webContents.send("city:find", city);
  addWindow.close();
});

//Custom menu template
const mainMenuTemplate = [
  {
    label: "File",
    submenu: [
      {
        label: "Enter city",
        accelerator: process.platform == "darwin" ? "Command+W" : "Ctrl+W",
        click() {
          createAddWindow();
        },
      },
      {
        label: "Exit",
        accelerator: process.platform == "darwin" ? "Command+Q" : "Ctrl+Q",
        click() {
          app.quit();
        },
      },
    ],
  },
];

//Modifies the menu for macOS
if (process.platform == "darwin") {
  mainMenuTemplate.unshift({});
}

//Adds developer tools
if (process.env.NODE_ENV !== "production") {
  mainMenuTemplate.push({
    label: "Developer Tools",
    submenu: [
      {
        label: "Dev tools",
        accelerator: process.platform == "darwin" ? "Command+I" : "Ctrl+I",
        click(e, focusedWindow) {
          focusedWindow.toggleDevTools();
        },
      },
      {
        role: "reload",
      },
    ],
  });
}