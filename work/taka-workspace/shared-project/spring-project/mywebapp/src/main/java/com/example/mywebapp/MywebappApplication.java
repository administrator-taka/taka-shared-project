package com.example.mywebapp;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.http.HttpStatus;
import org.springframework.http.MediaType;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;
@RestController

@SpringBootApplication
public class MywebappApplication {
	@RequestMapping("/")
	public String home() {
		return "Hello World";
	}
	public static void main(String[] args) {
		SpringApplication.run(MywebappApplication.class, args);
	}

}
