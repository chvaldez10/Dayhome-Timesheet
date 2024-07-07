Cypress.Commands.add("navigateToAttendancePage", () => {
  cy.log(`Navigating to attendance page`);
  cy.visit(Cypress.env("attendancePageUrl")).then(() => {
    cy.get("body").should("be.visible");
  });
});
