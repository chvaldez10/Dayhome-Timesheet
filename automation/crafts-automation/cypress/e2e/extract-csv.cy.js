describe("Extract CSV", () => {
  beforeEach(() => {
    cy.clearAllSessionStorage();
    cy.clearLocalStorage();
    cy.clearCookies();
    cy.visit("/");
  });

  it("login", () => {
    cy.login(Cypress.env("username"), Cypress.env("password"));
  });
});
