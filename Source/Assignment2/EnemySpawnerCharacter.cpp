// Fill out your copyright notice in the Description page of Project Settings.


#include "EnemySpawnerCharacter.h"

// Sets default values
AEnemySpawnerCharacter::AEnemySpawnerCharacter()
{
 	// Set this character to call Tick() every frame.  You can turn this off to improve performance if you don't need it.
	PrimaryActorTick.bCanEverTick = true;

}

void AEnemySpawnerCharacter::SpawnEnemy()
{


	if (UWorld* World = GetWorld())
	{
		if (Counter < SpawnLimit)
		{
			const FVector location = GetActorLocation();
			const FRotator rotator = GetActorRotation();
			FActorSpawnParameters Parameters;
			Counter += 1;
			World->SpawnActor(ClassToSpawn, &location, &rotator);

		}


	}
}

// Called when the game starts or when spawned
void AEnemySpawnerCharacter::BeginPlay()
{
	Super::BeginPlay();
	FTimerManager& TimerManager = GetWorldTimerManager();
	FTimerHandle SpawnTimerHandle;

	FTimerDelegate TimerDelegate;
	TimerDelegate.BindUObject(this, &AEnemySpawnerCharacter::SpawnEnemy);
	TimerManager.SetTimer(SpawnTimerHandle, TimerDelegate, SpawnTimer, true);
}

// Called every frame
void AEnemySpawnerCharacter::Tick(float DeltaTime)
{
	Super::Tick(DeltaTime);

}

// Called to bind functionality to input
void AEnemySpawnerCharacter::SetupPlayerInputComponent(UInputComponent* PlayerInputComponent)
{
	Super::SetupPlayerInputComponent(PlayerInputComponent);

}

