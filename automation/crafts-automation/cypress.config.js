const { defineConfig } = require("cypress");
require.config("dotenv");

module.exports = defineConfig({
  e2e: {
    setupNodeEvents(on, config) {
      dotenv.config({ path: ".env.local" });

      config.env.username = process.env.CRAFTS_USERNAME;
      config.env.password = process.env.CRAFTS_PASSWORD;

      return config;
    },
    baseUrl: process.env.CRAFTS_LOGIN_URL,
    viewportWidth: 1920,
    viewportHeight: 1080,
    defaultCommandTimeout: 7000,
  },
  env: {
    // Default values (optional)
    username: process.env.CRAFTS_USERNAME,
    password: process.env.CRAFTS_PASSWORD,
  },
});
