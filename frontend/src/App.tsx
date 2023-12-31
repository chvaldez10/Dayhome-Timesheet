import { BrowserRouter, Navigate, Route, Routes } from "react-router-dom";

import GlobalStyles from "./styles/GlobalStyles";
import Dashboard from "./pages/Dashboard";
import Settings from "./pages/Settings";
import Account from "./pages/Account";
import About from "./pages/About";
import ClassList from "./pages/ClassList";
import Login from "./pages/Login";
import PageNotFound from "./pages/PageNotFound";
import AppLayout from "./ui/AppLayout";

function App() {
  return (
    <>
      <GlobalStyles />
      <BrowserRouter>
        <Routes>
          <Route>
            <Route element={<AppLayout />}>
              <Route index element={<Navigate replace to="/dashboard" />} />
              <Route path="dashboard" element={<Dashboard />} />
              <Route path="class-list" element={<ClassList />} />
              <Route path="about" element={<About />} />
              <Route path="users" element={<Account />} />
              <Route path="settings" element={<Settings />} />
              <Route path="account" element={<Account />} />
            </Route>
            <Route path="login" element={<Login />} />
            <Route path="*" element={<PageNotFound />} />
          </Route>
        </Routes>
      </BrowserRouter>
    </>
  );
}

export default App;
