package com.example.myproject;

import org.springframework.data.repository.CrudRepository;
import org.springframework.stereotype.Repository;

@Repository
public interface UserRepository extends CrudRepository<User, String> {
    // No additional methods needed for basic CRUD operations
}
