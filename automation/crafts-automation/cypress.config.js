const { defineConfig } = require("cypress");
require("dotenv").config();

module.exports = defineConfig({
  e2e: {
    setupNodeEvents(on, config) {
      // Adding environment variables to Cypress config
      config.env.username = process.env.CRAFTS_USERNAME;
      config.env.password = process.env.CRAFTS_PASSWORD;

      return config;
    },
    baseUrl: process.env.CRAFTS_LOGIN_URL,
    viewportWidth: 1920,
    viewportHeight: 1080,
    defaultCommandTimeout: 10000,
    chromeWebSecurity: false,
  },
});
