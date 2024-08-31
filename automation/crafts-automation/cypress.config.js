const { defineConfig } = require("cypress");
require("dotenv").config();

module.exports = defineConfig({
  e2e: {
    setupNodeEvents(on, config) {
      // Adding environment variables to Cypress config
      config.env.username = process.env.CRAFTS_USERNAME;
      config.env.password = process.env.CRAFTS_PASSWORD;
      config.env.attendancePageUrl = process.env.CRAFTS_ATTENDANCE_URL;
      config.env.expectedCraftsCsv = process.env.EXPECTED_CRAFTS_CSV;

      return config;
    },
    baseUrl: process.env.CRAFTS_LOGIN_URL,
    viewportWidth: 1920,
    viewportHeight: 1080,
    defaultCommandTimeout: 7000,
    chromeWebSecurity: false,
    specPattern: "cypress/e2e/**/*.{js,jsx,ts,tsx}",
  },
});
