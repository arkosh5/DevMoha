// Fill out your copyright notice in the Description page of Project Settings.


#include "RoomPiece.h"

// Sets default values
ARoomPiece::ARoomPiece()
{
 	// Set this actor to call Tick() every frame.  You can turn this off to improve performance if you don't need it.
	PrimaryActorTick.bCanEverTick = true;

}

// Called when the game starts or when spawned
void ARoomPiece::BeginPlay()
{
	Super::BeginPlay();
}

// Called every frame
void ARoomPiece::Tick(float DeltaTime)
{
	Super::Tick(DeltaTime);

}

void ARoomPiece::OnConstruction(const FTransform& Transform)
{
	FRoomConfigs RoomConfigs;
	if (RoomStyle)
	{
		UStyle* Style = Cast<UStyle>(RoomStyle.GetDefaultObject());
		if (Style)
		{
			if (UWorld* World = GetWorld())
			{
				for (AActor* SpawnedActor : SpawnedActors)
				{
					if (SpawnedActor)
					{
						SpawnedActor->Destroy();
					}
				}

				SpawnedActors.Reset();
				if (Style->FloorPiece)
				{
					FVector Position = GetActorLocation() + RoomConfigs.RoomPosition;
					SpawnedActors.Add(World->SpawnActor(Style->FloorPiece, &Position));
				}

				if (Style->WallPiece)
				{
					FVector Position = GetActorLocation() + RoomConfigs.RoomPosition;
					SpawnedActors.Add(World->SpawnActor(Style->WallPiece, &Position));
				}

				if (Style->DoorPiece)
				{
					FVector Position = GetActorLocation() + RoomConfigs.RoomPosition;
					SpawnedActors.Add(World->SpawnActor(Style->DoorPiece, &Position));
				}

				if (Style->CornerPiece)
				{
					FVector Position = GetActorLocation() + RoomConfigs.RoomPosition;
					SpawnedActors.Add(World->SpawnActor(Style->CornerPiece, &Position));
				}
			}
		}


	}
}

void ARoomPiece::BuildRoom(FRoomConfigs)
{	//Build the room based on the configs.
	FRoomConfigs* Config;
	UStyle* Style = Cast<UStyle>(RoomStyle.GetDefaultObject());
	UStyle* Doors = Cast<UStyle>(Config->Doors.GetData());

		// Update the doors. 
		if (Doors)
		{
			// Spawn the doors.
			if (UWorld* World = GetWorld())
			{
				for (AActor* SpawnedActor : SpawnedActors)
				{
					if (SpawnedActor)
					{
						SpawnedActor->Destroy();
					}
				}

				SpawnedActors.Reset();
				if (Style->DoorPiece)
				{
					FVector Position = GetActorLocation() + FVector(0, 0, 0);
					SpawnedActors.Add(World->SpawnActor(Style->DoorPiece, &Position));
				}
			}
		}
		else
		{
			// Destroy the doors.
			if (UWorld* World = GetWorld())
			{
				for (AActor* SpawnedActor : SpawnedActors)
				{
					if (SpawnedActor)
					{
						SpawnedActor->Destroy();
					}
				}

				SpawnedActors.Reset();
			}
		}
		

		OnConstruction(GetTransform());
	
}

