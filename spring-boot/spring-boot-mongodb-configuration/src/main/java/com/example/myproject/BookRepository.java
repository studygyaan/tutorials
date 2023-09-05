package com.example.myproject;

import org.springframework.data.mongodb.repository.MongoRepository;
import org.springframework.stereotype.Repository;

@Repository
public interface BookRepository extends MongoRepository<Book, String> {
    // Additional custom queries can be defined here if needed
}
