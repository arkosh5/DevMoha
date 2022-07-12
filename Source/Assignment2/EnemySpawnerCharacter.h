// Fill out your copyright notice in the Description page of Project Settings.

#pragma once

#include <Assignment2/EnemyCharacter.h>
#include "CoreMinimal.h"
#include "GameFramework/Character.h"
#include "EnemySpawnerCharacter.generated.h"

UCLASS()
class ASSIGNMENT2_API AEnemySpawnerCharacter : public ACharacter
{
	GENERATED_BODY()

public:
	// Sets default values for this character's properties
	AEnemySpawnerCharacter();
	UPROPERTY(EditAnyWhere)
	TSubclassOf<AEnemyCharacter> ClassToSpawn;
	UPROPERTY(EditAnyWhere)
	int SpawnLimit = 0;
	UPROPERTY(EditAnyWhere)
	int SpawnTimer = 0;
private:
	int Counter;

protected:
	void SpawnEnemy();
	// Called when the game starts or when spawned
	virtual void BeginPlay() override;

public:	
	// Called every frame
	virtual void Tick(float DeltaTime) override;

	// Called to bind functionality to input
	virtual void SetupPlayerInputComponent(class UInputComponent* PlayerInputComponent) override;

};
