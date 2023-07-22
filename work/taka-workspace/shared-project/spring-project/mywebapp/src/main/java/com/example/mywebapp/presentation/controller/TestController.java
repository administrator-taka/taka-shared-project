package com.example.mywebapp.presentation.controller;

import com.example.mywebapp.application.service.TestService;
import com.example.mywebapp.presentation.request.TestRequest;
import lombok.RequiredArgsConstructor;
import org.springframework.http.HttpStatus;
import org.springframework.http.MediaType;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequestMapping("/test")
@RequiredArgsConstructor
public class TestController {

  private final TestService testService;

  @RequestMapping("/")
  public String home() {
    return "Hello World";
  }

  @PostMapping(consumes = MediaType.APPLICATION_JSON_VALUE, produces = MediaType.APPLICATION_JSON_VALUE)
  public ResponseEntity<?> test(@RequestBody String str) {
    System.out.println("test");
    return ResponseEntity.status(HttpStatus.OK).body(str);
  }

  @PostMapping(path = "/db", consumes = MediaType.APPLICATION_JSON_VALUE, produces = MediaType.APPLICATION_JSON_VALUE)
  public ResponseEntity<?> testDb(@RequestBody TestRequest request) {
    System.out.println("リクエスト出力:" + request);
    testService.test(request.getTest());
    return ResponseEntity.status(HttpStatus.OK).body(request);
  }
}
