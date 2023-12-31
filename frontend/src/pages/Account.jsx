import Heading from "../ui/Heading";
import Row from "../ui/Row";

function Account() {
  return (
    <>
      <Heading>Update your account</Heading>
      <Row>
        <Heading as="h3"> Update your data</Heading>
      </Row>
      <Row>
        <Heading as="h3"> Update your password</Heading>
      </Row>
    </>
  );
}

export default Account;
