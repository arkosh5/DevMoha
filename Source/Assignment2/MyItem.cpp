// Fill out your copyright notice in the Description page of Project Settings.


#include "MyItem.h"
#include "PlayerCharacter.h"

// Sets default values
AMyItem::AMyItem()
{
 	// Set this actor to call Tick() every frame.  You can turn this off to improve performance if you don't need it.
	PrimaryActorTick.bCanEverTick = true;
	Mushroom = CreateDefaultSubobject<UStaticMeshComponent>(TEXT("Mushroom"));
	Poision = CreateDefaultSubobject<UStaticMeshComponent>(TEXT("Poision"));
	Scale = CreateDefaultSubobject<UStaticMeshComponent>(TEXT("Scale"));
	Health = CreateDefaultSubobject<UStaticMeshComponent>(TEXT("Health"));
}

void AMyItem::OnOverlapBegin(UPrimitiveComponent* OverlappedComp, AActor* OtherActor, UPrimitiveComponent* OtherComp, int32 OtherBodyIndex, bool bFromSweep, const FHitResult& SweepResult)
{
	//if player overlap with mushroom destroy mushroom
	
		APlayerCharacter* Player = Cast<APlayerCharacter>(OtherActor);
		// if player overlap with mushroom then destroy mushroom
		if (Player)
		{
			if (Mushroom)
			{
				Destroy();
			}
			if (Scale)
			{
				Destroy();
			}
			//if player overlap with health destroy health and increase player health
			if (Health)
			{
				Destroy();
				if (Player)
				{
					Player->Health += 10;
				}
			}
			//if player overlap with poision destroy poision and decrease player health
			if (Poision)
			{
				Destroy();
			}
		}
}

// Called when the game starts or when spawned
void AMyItem::BeginPlay()
{
	Super::BeginPlay();
	// bind to the mushroom component's overlap begin event
	Mushroom->OnComponentBeginOverlap.AddDynamic(this, &AMyItem::OnOverlapBegin);
	// bind to the scale component's overlap begin event
	Scale->OnComponentBeginOverlap.AddDynamic(this, &AMyItem::OnOverlapBegin);
	// bind to the health component's overlap begin event
	Health->OnComponentBeginOverlap.AddDynamic(this, &AMyItem::OnOverlapBegin);
	// bind to the poision component's overlap begin event
	Poision->OnComponentBeginOverlap.AddDynamic(this, &AMyItem::OnOverlapBegin);


}

// Called every frame
void AMyItem::Tick(float DeltaTime)
{
	Super::Tick(DeltaTime);

}

