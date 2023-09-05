package com.example.myproject;

import org.apache.camel.CamelContext;
import org.apache.camel.builder.RouteBuilder;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

@Configuration
public class MyRouterConfiguration {

    @Autowired
    private CamelContext camelContext;

    @Bean
    public RouteBuilder myRoute() {
        return new RouteBuilder() {
            public void configure() {
                from("timer:foo?period=5000")
                        .setBody().constant("Hello, world!")
                        .to("log:foo");
            }
        };
    }
}