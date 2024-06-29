describe("Extract CSV", () => {
  beforeEach(() => {
    cy.clearAllSessionStorage();
    cy.clearLocalStorage();
    cy.clearCookies();
    cy.visit("/");
  });

  it("login", () => {
    cy.log("Hello World");
  });
});
