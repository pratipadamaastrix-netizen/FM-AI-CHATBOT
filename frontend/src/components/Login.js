import { useState, useContext } from "react";
import { TextField, Button, Container, Typography } from "@mui/material";
import API from "../api/axios";
import { AuthContext } from "../context/AuthContext";

function Login() {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const { login } = useContext(AuthContext);

  const handleLogin = async () => {
    const res = await API.post("/login", { email, password });
    login(res.data.access_token);
  };

  return (
    <Container maxWidth="sm">
      <Typography variant="h4" gutterBottom>Admin Login</Typography>
      <TextField fullWidth label="Email" margin="normal"
        onChange={(e) => setEmail(e.target.value)} />
      <TextField fullWidth label="Password" type="password" margin="normal"
        onChange={(e) => setPassword(e.target.value)} />
      <Button fullWidth variant="contained" onClick={handleLogin}>
        Login
      </Button>
    </Container>
  );
}

export default Login;