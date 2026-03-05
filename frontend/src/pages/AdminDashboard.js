import { useEffect, useState } from "react";
import { Table, TableRow, TableCell, TableHead, TableBody, Button } from "@mui/material";
import API from "../api/axios";

function AdminDashboard() {
  const [tickets, setTickets] = useState([]);

  const fetchTickets = async () => {
    const res = await API.get("/tickets");
    setTickets(res.data);
  };

  useEffect(() => {
    fetchTickets();
    const interval = setInterval(fetchTickets, 5000); // live update
    return () => clearInterval(interval);
  }, []);

  const updateStatus = async (id, status) => {
    await API.put(`/tickets/${id}`, { status });
    fetchTickets();
  };

  return (
    <Table>
      <TableHead>
        <TableRow>
          <TableCell>Reference</TableCell>
          <TableCell>Status</TableCell>
          <TableCell>Change</TableCell>
        </TableRow>
      </TableHead>
      <TableBody>
        {tickets.map(ticket => (
          <TableRow key={ticket.id}>
            <TableCell>{ticket.reference}</TableCell>
            <TableCell>{ticket.status}</TableCell>
            <TableCell>
              <Button onClick={() => updateStatus(ticket.id, "Closed")}>
                Close
              </Button>
            </TableCell>
          </TableRow>
        ))}
      </TableBody>
    </Table>
  );
}

export default AdminDashboard;