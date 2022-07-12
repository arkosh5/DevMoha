// Fill out your copyright notice in the Description page of Project Settings.

#pragma once

#include "CoreMinimal.h"
#include "Style.h"
#include "GameFramework/Actor.h"
#include "RoomPiece.generated.h"



UENUM(BluePrintType)
enum class EWall : uint8
{
	North,
	East,
	South,
	West
};

USTRUCT()
struct FDoor
{
	GENERATED_BODY()
public:
	UPROPERTY(EditAnywhere)
	EWall Wall;
	UPROPERTY(EditAnywhere)
	int PositionOnWall = 0;
};

USTRUCT(BluePrintType)
struct FRoomConfigs
{
	GENERATED_BODY()
public:
	UPROPERTY(EditAnywhere)
	FVector2D RoomSize;
	UPROPERTY(EditAnywhere)
	TArray<FDoor> Doors;
	UPROPERTY(EditAnywhere)
	FVector RoomPosition;
	
	static UStyle* Style;


};

UCLASS()
class ASSIGNMENT2_API ARoomPiece : public AActor
{
	GENERATED_BODY()
	
public:	
	// Sets default values for this actor's properties
	ARoomPiece();
	

protected:
	// Called when the game starts or when spawned
	virtual void BeginPlay() override;

public:	
	// Called every frame
	virtual void Tick(float DeltaTime) override;
	virtual void OnConstruction(const FTransform& Transform) override;
	void BuildRoom(FRoomConfigs);
	UPROPERTY(EditAnywhere)
	TSubclassOf<UStyle> RoomStyle;
	TArray<AActor*> SpawnedActors;
	UPROPERTY(EditAnywhere)
	TArray<FRoomConfigs> Configs;
};
