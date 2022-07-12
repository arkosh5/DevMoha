// Fill out your copyright notice in the Description page of Project Settings.


#include "EnemyCharacter.h"
#include "Components/SphereComponent.h"
#include "GameFramework/CharacterMovementComponent.h"
#include <Runtime/Engine/Classes/Kismet/GameplayStatics.h>
#include <Assignment2/Assignment2GameMode.h>

// Sets default values
AEnemyCharacter::AEnemyCharacter()
	:Health(100)
{
	// Set this character to call Tick() every frame.  You can turn this off to improve performance if you don't need it.
	PrimaryActorTick.bCanEverTick = true;

	PlayerDetectionSphere = CreateDefaultSubobject<USphereComponent>(FName("PlayerDetectionSphere"));
	AttackRadiusSphere = CreateDefaultSubobject<USphereComponent>(FName("AttackRadiusSphere"));

	if (RootComponent)
	{
		if (AttackRadiusSphere)
		{
			AttackRadiusSphere->SetSphereRadius(AttackRadius);

			// Make sure it's attached to the root component
			AttackRadiusSphere->AttachToComponent(RootComponent, FAttachmentTransformRules::KeepRelativeTransform);
		}
		
		if (PlayerDetectionSphere)
		{
			PlayerDetectionSphere->SetSphereRadius(PlayerDetectionRadius);

			// Make sure it's attached to the root component
			PlayerDetectionSphere->AttachToComponent(RootComponent, FAttachmentTransformRules::KeepRelativeTransform);
		}
	}
	
}

void AEnemyCharacter::OnOverlapBegin(UPrimitiveComponent* OverlappedComp, AActor* OtherActor, UPrimitiveComponent* OtherComp, int32 OtherBodyIndex, bool bFromSweep, const FHitResult& SweepResult)
{
	APlayerCharacter* Player = Cast<APlayerCharacter>(OtherActor);
	// if player overlap with attack radius then attack player and stop movement
	if (Player)
	{
		if (AttackRadiusSphere)
		{
			// stop movement
			GetCharacterMovement()->StopMovementImmediately();
		}
		if (PlayerDetectionSphere)
		{
			// start Movement
			GetCharacterMovement()->SetMovementMode(MOVE_Walking);

		}
		
	}

}

void AEnemyCharacter::OnOverlapEnd(class UPrimitiveComponent* OverlappedComp, class AActor* OtherActor, class UPrimitiveComponent* OtherComp, int32 OtherBodyIndex)
{
	APlayerCharacter* Player = Cast<APlayerCharacter>(OtherActor);
	// if player overlap with attack radius then attack player and stop movement
	if (Player)
	{
		if (AttackRadiusSphere)
		{
			// start Movement
			GetCharacterMovement()->SetMovementMode(MOVE_Walking);
		}
		if (PlayerDetectionSphere)
		{
			// stop Movement
			GetCharacterMovement()->StopMovementImmediately();
		}
	}
}

// Called when the game starts or when spawned
void AEnemyCharacter::BeginPlay()
{
	Super::BeginPlay();
	PlayerDetectionSphere->OnComponentBeginOverlap.AddDynamic(this, &AEnemyCharacter::OnOverlapBegin);
	AttackRadiusSphere->OnComponentBeginOverlap.AddDynamic(this, &AEnemyCharacter::OnOverlapBegin);
}

// Called every frame
void AEnemyCharacter::Tick(float DeltaTime)
{
	Super::Tick(DeltaTime);
	UCharacterMovementComponent* CharacterMovment = Cast<UCharacterMovementComponent>(GetMovementComponent());
	APlayerCharacter* PlayerCharacter = Cast<APlayerCharacter>(UGameplayStatics::GetPlayerCharacter(GetWorld(), 0));

	// get player location as FVector
	FVector PlayerLocation = PlayerCharacter->GetActorLocation();
	// get enemy location as FVector
	FVector EnemyLocation = GetActorLocation();
	// get distance between player as FVector
	FVector Distance = PlayerLocation - EnemyLocation;
	
	
	// if distance between player and enemy is less than player detection radius
	if (Distance.Size() < PlayerDetectionRadius)
	{
		CharacterMovment->AddInputVector(Distance);
	}
}

// Called to bind functionality to input
void AEnemyCharacter::SetupPlayerInputComponent(UInputComponent* PlayerInputComponent)
{
	Super::SetupPlayerInputComponent(PlayerInputComponent);

}

