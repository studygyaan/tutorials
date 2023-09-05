package com.example.myproject;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

@RestController
@RequestMapping("/users")
public class UserController {

    private final UserService userService;

    @Autowired
    public UserController(UserService userService) {
        this.userService = userService;
    }

    @PostMapping
    public User createUser(@RequestBody User user) {
        return userService.saveUser(user);
    }

    @GetMapping("/{id}")
    public User getUserById(@PathVariable String id) {
        return userService.getUserById(id).orElse(null);
    }

    @GetMapping
    public Iterable<User> getAllUsers() {
        return userService.getAllUsers();
    }

    @DeleteMapping("/{id}")
    public void deleteUser(@PathVariable String id) {
        userService.deleteUser(id);
    }
}
