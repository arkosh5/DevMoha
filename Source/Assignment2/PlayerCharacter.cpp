// Fill out your copyright notice in the Description page of Project Settings.


#include "PlayerCharacter.h"
#include "MyItem.h"
#include "Assignment2GameMode.h"
#include "EnemyCharacter.h"
#include "Kismet/GameplayStatics.h"

// Sets default values
APlayerCharacter::APlayerCharacter()
	:Health(0),Damage(0)
{
 	// Set this character to call Tick() every frame.  You can turn this off to improve performance if you don't need it.
	PrimaryActorTick.bCanEverTick = true;

	// Attach a sword mesh to the character mesh
	SwordMesh = CreateDefaultSubobject<UStaticMeshComponent>(FName("SwordMesh"));
	SwordMesh->AttachToComponent(GetMesh(), FAttachmentTransformRules::KeepRelativeTransform, FName("Hand_R"));
	
}

void APlayerCharacter::OnOverlapBegin(UPrimitiveComponent* OverlappedComp, AActor* OtherActor, UPrimitiveComponent* OtherComp, int32 OtherBodyIndex, bool bFromSweep, const FHitResult& SweepResult)
{
	
	// If the other actor is an enemy, print a message and deal damage to it.
	if (OtherActor->IsA(AEnemyCharacter::StaticClass()))
	{
		AEnemyCharacter* Enemy = Cast<AEnemyCharacter>(OtherActor);
		// if the sword is attacking a valid target, deacrease the enemy's health.
		if (Enemy)
		{
			Damage = FMath::RandRange(5, 25);
			if (IsAttacking())
			{
				StopAttacking();
				if (AGameModeBase* GameMode = UGameplayStatics::GetGameMode(this))
				{
					// Cast it to our specific game mode
					if (AAssignment2GameMode* AssignmentGameMode = Cast<AAssignment2GameMode>(GameMode))
					{
						// Send a basic message
						FStringFormatNamedArguments Arguments;
						Arguments.Add(FString("AMOUNT"), FStringFormatArg(Damage));
						FString Text = FString::Format(TEXT("Yes!I did{AMOUNT}" ), Arguments);
						AssignmentGameMode->SendCharacterMessage(Text);
					}
				}
			}

			// if the enemy's health is 0 or less, destroy the enemy.
			if (Enemy->Health <= 0)
			{
				Enemy->Destroy();
			}
		}


	}
}

// Called when the game starts or when spawned
void APlayerCharacter::BeginPlay()
{
	Super::BeginPlay();
	SwordMesh->OnComponentBeginOverlap.AddDynamic(this, &APlayerCharacter::OnOverlapBegin);
	SwordMesh->SetCollisionProfileName(FName("Trigger"));
	SwordMesh->SetGenerateOverlapEvents(true);
}

// Called every frame
void APlayerCharacter::Tick(float DeltaTime)
{
	Super::Tick(DeltaTime);

}

// Called to bind functionality to input
void APlayerCharacter::SetupPlayerInputComponent(UInputComponent* PlayerInputComponent)
{
	Super::SetupPlayerInputComponent(PlayerInputComponent);

}

