describe("Extract CSV", () => {
  beforeEach(() => {
    cy.clearAllSessionStorage();
    cy.clearLocalStorage();
    cy.clearCookies();
    cy.visit("/");
  });

  Cypress.on("uncaught:exception", (err, runnable) => {
    // returning false to prevent test from failing because of website
    return false;
  });

  it("login", () => {
    cy.login(Cypress.env("username"), Cypress.env("password"));
    cy.navigateToAttendancePage();
    cy.traverseDate(7, 2024, "July");
  });
});
