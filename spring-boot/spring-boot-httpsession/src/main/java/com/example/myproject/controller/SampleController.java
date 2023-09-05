package com.example.myproject.controller;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpSession;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequestMapping("/api")
public class SampleController {

    @GetMapping("/hello")
    public String sayHello() {
        return "Hello, Spring Boot!";
    }

    @GetMapping("/storeData")
    public String storeData(HttpServletRequest request) {
        HttpSession session = request.getSession();
        // Store data in the session
        session.setAttribute("username", "john_doe");
        return "data_stored";
    }

    @GetMapping("/getData")
    public String getData(HttpSession session) {
        String username = (String) session.getAttribute("username");
        return "Hello, " + username;
    }

    @GetMapping("/logout")
    public String logout(HttpSession session) {
        // Invalidate the session
        session.invalidate();
        return "logged_out";
    }


}