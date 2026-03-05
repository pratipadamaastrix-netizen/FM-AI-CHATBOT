import { useState, useEffect, useRef } from "react";
import {
  Box,
  Typography,
  TextField,
  IconButton,
  Paper,
  Chip
} from "@mui/material";
import SendIcon from "@mui/icons-material/Send";
import AddIcon from "@mui/icons-material/Add";
import CloseIcon from "@mui/icons-material/Close";
import API from "../api/axios";
import "../App.css";

function ChatWidget() {
  const [messages, setMessages] = useState([]);
  const [input, setInput] = useState("");
  const [file, setFile] = useState(null);
  const [preview, setPreview] = useState(null);

  const chatBodyRef = useRef(null);
  const fileInputRef = useRef(null);

  // ✅ Auto Scroll
  useEffect(() => {
    if (chatBodyRef.current) {
      chatBodyRef.current.scrollTo({
        top: chatBodyRef.current.scrollHeight,
        behavior: "smooth",
      });
    }
  }, [messages]);

  // ✅ Handle File Selection
  const handleFileChange = (e) => {
    const selectedFile = e.target.files[0];
    if (!selectedFile) return;

    setFile(selectedFile);

    if (selectedFile.type.startsWith("image/")) {
      const reader = new FileReader();
      reader.onloadend = () => {
        setPreview(reader.result);
      };
      reader.readAsDataURL(selectedFile);
    } else {
      setPreview(null);
    }
  };

  // ✅ Remove Selected File
  const removeFile = () => {
    setFile(null);
    setPreview(null);
    if (fileInputRef.current) {
      fileInputRef.current.value = "";
    }
  };

  const sendMessage = async () => {
    if (!input.trim() && !file) return;

    const userMessage = {
      role: "user",
      content: input || "",
      fileName: file?.name || null,
      preview: preview || null,
    };

    setMessages((prev) => [...prev, userMessage]);

    try {
      const formData = new FormData();
      formData.append("user_name", "Alice");
      formData.append("location_estate", "Block B");
      formData.append("location_unit", "101");
      formData.append("problem_description", input || "");

      if (file) {
        formData.append("file", file);
      }

      const res = await API.post("/api/chat", formData);

      console.log("API RESPONSE:", res.data);

      setMessages((prev) => [
        ...prev,
        {
          role: "bot",
          content:
            res?.data?.bot_reply ||
            "Response received but bot_reply not found.",
        },
      ]);
    } catch (error) {
      console.error("API ERROR:", error);

      setMessages((prev) => [
        ...prev,
        {
          role: "bot",
          content: "Server error. Please try again.",
        },
      ]);
    }

    setInput("");
    removeFile();
  };

  return (
    <Box className="chat-wrapper">
      <Paper className="chat-card" elevation={10}>

        {/* Header */}
        <Box className="chat-header">
          <Typography variant="h6">Facility AI Support</Typography>
          <Typography variant="body2">
            Talk with us. We're here to help.
          </Typography>
        </Box>

        {/* Chat Body */}
        <Box className="chat-body" ref={chatBodyRef}>
          {messages.map((msg, index) => (
            <Box
              key={index}
              className={`chat-bubble ${
                msg.role === "user" ? "user" : "bot"
              }`}
            >
              {msg.content && <Typography>{msg.content}</Typography>}

              {msg.preview && (
                <img
                  src={msg.preview}
                  alt="preview"
                  style={{
                    marginTop: 8,
                    maxWidth: "200px",
                    borderRadius: "8px",
                  }}
                />
              )}

              {msg.fileName && !msg.preview && (
                <Typography variant="caption">
                  📎 {msg.fileName}
                </Typography>
              )}
            </Box>
          ))}
        </Box>

        {/* Selected File Preview */}
        {file && (
          <Box sx={{ p: 1, display: "flex", alignItems: "center", gap: 1 }}>
            {preview ? (
              <img
                src={preview}
                alt="preview"
                style={{ maxWidth: 80, borderRadius: 6 }}
              />
            ) : (
              <Chip label={file.name} />
            )}

            <IconButton size="small" onClick={removeFile}>
              <CloseIcon fontSize="small" />
            </IconButton>
          </Box>
        )}

        {/* Input Section */}
        <Box className="chat-input">
          <input
            type="file"
            ref={fileInputRef}
            style={{ display: "none" }}
            onChange={handleFileChange}
          />

          <IconButton component="label" color="primary">
            <AddIcon />
            <input
              type="file"
              hidden
              ref={fileInputRef}
              onChange={handleFileChange}
            />
          </IconButton>

          <TextField
            fullWidth
            placeholder="Type your message..."
            variant="outlined"
            size="small"
            value={input}
            onChange={(e) => setInput(e.target.value)}
            onKeyDown={(e) => e.key === "Enter" && sendMessage()}
          />

          <IconButton color="primary" onClick={sendMessage}>
            <SendIcon />
          </IconButton>
        </Box>

      </Paper>
    </Box>
  );
}

export default ChatWidget;