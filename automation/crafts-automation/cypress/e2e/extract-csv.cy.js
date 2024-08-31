describe("Extract CSV", () => {
  beforeEach(() => {
    cy.clearAllSessionStorage();
    cy.clearLocalStorage();
    cy.clearCookies();
    cy.visit("/");
  });

  Cypress.on("uncaught:exception", (err, runnable) => {
    // returning false to prevent test from failing
    return false;
  });

  it("Extract csv files", () => {
    cy.login(Cypress.env("username"), Cypress.env("password"));
    cy.navigateToAttendancePage();
    cy.traverseDate(8, 2024, "August");
  });
});
