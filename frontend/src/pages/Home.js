import { Container, Typography } from "@mui/material";
import ChatWidget from "../components/ChatWidget";

function Home() {
  return (
    <Container sx={{ mt: 4 }}>
      <Typography variant="h4" gutterBottom>
        Facility Management Chatbot
      </Typography>
      <ChatWidget />
    </Container>
  );
}

export default Home;