// The official FreeTheAI Go SDK: one reply, then a streamed reply.
//
//	go run .
//	FREETHEAI_API_KEY=ftai_... go run .
package main

import (
	"context"
	"fmt"
	"log"

	"github.com/Free-The-Ai/freetheai-go"
)

func main() {
	client, err := freetheai.NewClient() // reads FREETHEAI_API_KEY
	if err != nil {
		log.Fatal(err)
	}
	ctx := context.Background()

	reply, err := client.Chat.Completions.New(ctx, freetheai.ChatCompletionParams{
		Model:    "fta/zai/glm-5.3",
		Messages: []freetheai.Message{{Role: "user", Content: "Write a haiku about open models."}},
	})
	if err != nil {
		log.Fatal(err)
	}
	fmt.Println(reply.Choices[0].Message.Content)

	fmt.Println("\nStreamed:")
	stream, err := client.Chat.Completions.NewStreaming(ctx, freetheai.ChatCompletionParams{
		Model:    "fta/zai/glm-5.3-flash",
		Messages: []freetheai.Message{{Role: "user", Content: "Count from one to five, one word per line."}},
	})
	if err != nil {
		log.Fatal(err)
	}
	defer stream.Close()
	for stream.Next() {
		for _, choice := range stream.Current().Choices {
			fmt.Print(choice.Delta.Content)
		}
	}
	if err := stream.Err(); err != nil {
		log.Fatal(err)
	}
	fmt.Println()
}
