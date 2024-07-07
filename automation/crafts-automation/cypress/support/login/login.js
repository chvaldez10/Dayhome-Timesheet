Cypress.Commands.add("login", (username, password) => {
  cy.log("Attempting to login");
  cy.get('.form-group input[placeholder="Email"]').type(username);
  cy.get('.form-group input[placeholder="Password"]').type(password);

  cy.log("Manually need to click GAPTCHA");
  cy.get("iframe")
    .first()
    .then((recaptchaIframe) => {
      const body = recaptchaIframe.contents().find("body");
      cy.wrap(body)
        .find(".recaptcha-checkbox-border")
        .should("be.visible")
        .click();
    });
  cy.pause();

  cy.log(`Resuming login after GAPTCHA`);
  cy.get('button[id="submitBtn"]').click();
});
