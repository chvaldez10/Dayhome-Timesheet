import styled from "styled-components";

const StyledLogo = styled.div`
  text-align: center;
`;

const Img = styled.img`
  width: auto;
`;

function Logo() {
  return (
    <StyledLogo>
      <Img src="/radiance-logo-no-bg.png" />
    </StyledLogo>
  );
}

export default Logo;
