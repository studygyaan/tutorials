package com.example.myproject;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping("/books")
public class BookController {
    private final BookService bookService;

    @Autowired
    public BookController(BookService bookService) {
        this.bookService = bookService;
    }

    @PostMapping
    public Book createBook(@RequestBody Book book) {
        return bookService.createBook(book);
    }

    @GetMapping
    public List<Book> getAllBooks() {
        return bookService.getAllBooks();
    }

    @GetMapping("/{id}")
    public Book getBookById(@PathVariable String id) {
        return bookService.getBookById(id).orElse(null);
    }

    @PutMapping("/{id}")
    public Book updateBook(@PathVariable String id, @RequestBody Book book) {
        book.setId(id);
        return bookService.updateBook(book);
    }

    @DeleteMapping("/{id}")
    public void deleteBook(@PathVariable String id) {
        bookService.deleteBook(id);
    }
}
