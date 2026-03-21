# 🌱 COFFEE VARIETALS — COMPREHENSIVE GENETIC INTELLIGENCE

**Complete variety database for Alternative Coffee Claude**
**Version 2.0 — Enhanced with Python-style data structures and Drip on Ice brewing**

---

## 📋 CLASSIFICATION HIERARCHY

```python
coffee_species_tree = {
    "genus": "Coffea",
    "species_count": 124,
    "commercially_significant": 2,
    
    "arabica": {
        "scientific_name": "Coffea arabica",
        "global_production_percent": 60,
        "chromosome_count": 44,  # diploid
        "self_pollinating": True,
        
        "lineages": {
            "typica": {
                "origin": "Ethiopia → Yemen → Java → Americas",
                "varieties": ["Typica", "Maragogype", "Kent", "SL28", "SL34", "Blue Mountain"]
            },
            "bourbon": {
                "origin": "Réunion island (Île Bourbon)",
                "varieties": ["Red Bourbon", "Yellow Bourbon", "Pink Bourbon", "Caturra", "Catuai", "Pacamara"]
            },
            "ethiopian_heirlooms": {
                "origin": "Ethiopia (wild diversity)",
                "genetic_profiles": ">1000",
                "regions": ["Yirgacheffe", "Sidamo", "Harrar", "Limu", "Gesha"]
            },
            "modern_hybrids": {
                "f1_hybrids": ["Centroamericano", "Starmaya", "Evaluna"],
                "introgressed": ["Catimor", "Castillo", "Ruiru 11", "Batian"],
                "note": "Introgressed = Robusta genes for disease resistance"
            }
        }
    },
    
    "robusta": {
        "scientific_name": "Coffea canephora",
        "global_production_percent": 40,
        "chromosome_count": 22,  # diploid, different from arabica
        "self_pollinating": False,  # cross-pollinating
        "varieties": ["Robusta", "Conilon", "Nganda"]
    }
}
```

---

## ☕ TYPICA — Foundation Variety

```python
typica = {
    "genetics": {
        "origin": "Ethiopia → Yemen (1400s) → Java (1600s) → Americas (1700s)",
        "genetic_diversity": "LOW (bottleneck from limited seed transport)",
        "lineage": "Foundation for 90% of Latin American arabica"
    },
    
    "morphology": {
        "tree_height_m": (3, 4),  # range
        "branch_angle_degrees": (50, 70),
        "leaf": "Long, narrow, bronze tips when young",
        "cherry_shape": "Elongated oval",
        "bean_shape": "Long, narrow",
        "screen_size": (18, 19)
    },
    
    "agronomy": {
        "yield_kg_per_ha": (1000, 1500),
        "yield_rating": "2/10 (LOW)",
        "disease_resistance": {
            "coffee_leaf_rust": "1/10 (VERY LOW)",
            "coffee_berry_disease": "2/10 (LOW)",
            "nematodes": "3/10 (LOW)"
        },
        "climate": {
            "optimal_temp_c": (18, 22),
            "altitude_masl": (1000, 2000),
            "rainfall_mm": (1500, 2500),
            "frost_tolerance": "LOW"
        },
        "productive_years": (20, 30),
        "peak_production_years": (7, 15)
    },
    
    "chemistry_at_1500masl": {
        "sugars_percent": (9, 11),
        "caffeine_percent": (1.2, 1.5),
        "chlorogenic_acids_percent": (6.5, 8.5),
        "lipids_percent": (15, 17),
        "proteins_percent": (11, 13),
        "organic_acids": {
            "malic": "HIGH (apple-like)",
            "citric": "MEDIUM-HIGH",
            "quinic": "MEDIUM"
        }
    },
    
    "flavor_profile": {
        "acidity": "Bright, malic acid dominance",
        "body": "Light-medium, tea-like",
        "sweetness": "High when properly developed",
        "complexity": "Excellent (clean, layered)",
        "notes": ["Floral", "Citrus", "Stone fruit", "Honey"],
        "aftertaste": "Long, clean, sweet"
    },
    
    "roasting_physics": {
        "bean_density_g_per_cm3": (0.70, 0.75),  # HIGH at altitude
        "moisture_percent": (10, 12),
        "first_crack_temp_c": (196, 202),
        "development_time_ratio_percent": (18, 22),
        "drop_temp_c": (202, 208),
        "roast_level": "Light to Light-Medium",
        
        "profile_targets": {
            "charge_temp_c": (195, 200),
            "turning_point_c": (95, 100),
            "maillard_duration_min": (3.5, 4.5),
            "development_duration_min": (1.5, 2.0),
            "total_time_min": (9, 11)
        }
    },
    
    "brewing": {
        "pour_over_v60": {
            "dose_g": 20,
            "water_g": 320,
            "ratio": "1:16",
            "temp_c": (93, 95),
            "grind_comandante": (22, 24),
            "time_min": (3.0, 3.5)
        },
        
        "drip_on_ice": {
            "dose_g": 30,
            "hot_water_g": 220,
            "ice_in_server_g": 80,
            "total_yield_g": 300,
            "ratio": "1:10 (final)",
            "effective_brew_ratio": "1:7.3 (before ice)",
            "temp_c": (94, 96),
            "grind_comandante": (20, 22),
            "time_min": (2.5, 3.0),
            "flavor_impact": "Bright acidity shines, floral notes locked by instant chill"
        },
        
        "espresso": {
            "dose_g": 18,
            "yield_g": (36, 40),
            "time_sec": (25, 30),
            "temp_c": (93, 94),
            "note": "High clarity, tea-like espresso"
        }
    },
    
    "economics": {
        "green_price_usd_per_kg": (3.5, 6.0),
        "premium_vs_commodity_percent": (40, 80),
        "market_segment": "Specialty (83+ SCA)",
        
        "farmer_perspective": {
            "pros": ["Premium price", "Excellent cup quality", "Market recognition"],
            "cons": ["Low yield", "High disease risk", "Labor intensive"],
            "viable_only_if": [
                "Premium market access ($5+/kg)",
                "Disease management capability",
                "Can tolerate low yield"
            ]
        }
    },
    
    "alternative_slowbar_verdict": {
        "quality_rating": "9/10",
        "yield_rating": "2/10",
        "disease_risk_rating": "9/10 (very high)",
        "farmer_viability": "4/10",
        
        "honest_assessment": """
Beautiful coffee, terrible economics.
Plant Typica ONLY if:
  1. Premium buyers confirmed ($5+/kg)
  2. Disease management budget + expertise
  3. Value quality over quantity

Otherwise: Plant Bourbon, Caturra, or F1 hybrids
        """
    }
}
```

---

## ☕ GEISHA — Ultra-Premium Variety

```python
geisha = {
    "genetics": {
        "origin": "Gesha village, Ethiopia (1930s collection)",
        "panama_transplant": "1960s (exploded in fame 2004)",
        "genetic_distinctness": "HIGH (distinct from other Ethiopian types)"
    },
    
    "morphology": {
        "tree_height_m": (4, 5),  # VERY tall
        "structure": "Sparse, willowy, open branching",
        "leaf": "Long, thin, bronze tips",
        "bean_shape": "Very long, narrow",
        "screen_size": (19, 20),
        "bean_density_g_per_cm3": (0.72, 0.78)  # VERY HIGH
    },
    
    "agronomy": {
        "yield_kg_per_ha": (600, 1000),  # VERY LOW
        "yield_rating": "1/10 (VERY LOW)",
        "yield_vs_caturra_percent": -60,
        
        "disease_resistance": {
            "coffee_leaf_rust": "1/10 (VERY LOW)",
            "coffee_berry_disease": "2/10 (LOW)",
            "management": "Constant monitoring required"
        },
        
        "climate": {
            "optimal_temp_c": (16, 20),  # Cool
            "altitude_masl": (1500, 2000),  # HIGH essential
            "rainfall_mm": (2000, 3000),
            "terroir_specificity": "EXTREMELY HIGH"
        }
    },
    
    "chemistry_panama_1700masl": {
        "sugars_percent": (10, 12),  # Very high
        "caffeine_percent": (1.1, 1.3),
        
        "volatile_compounds_mg_per_kg": {
            "linalool": (15, 25),  # VERY HIGH (jasmine aroma)
            "geraniol": (8, 15),  # HIGH (rose aroma)
            "beta_damascenone": (0.5, 1.5),  # Tea-like
            "note": "Floral volatiles 2-3x higher than Typica"
        },
        
        "organic_acids": {
            "citric": "VERY HIGH",
            "malic": "HIGH",
            "phosphoric": "MEDIUM (varies by terroir)"
        }
    },
    
    "flavor_profile": {
        "acidity": "Very bright, complex (citric + malic)",
        "body": "Very light, tea-like, delicate",
        "sweetness": "Exceptional (honey, sugar cane)",
        "complexity": "Extraordinary (layered, evolving)",
        "signature_notes": ["Jasmine", "Bergamot", "Earl Grey tea", "Tropical fruit"],
        "aftertaste": "Very long, floral, sweet"
    },
    
    "roasting_physics": {
        "bean_density_g_per_cm3": (0.72, 0.78),  # VERY high
        "first_crack_temp_c": (198, 205),  # Late due to density
        "development_time_ratio_percent": (18, 22),
        "drop_temp_c": (200, 206),
        "roast_level": "Light ONLY",
        
        "critical_temperatures": {
            "linalool_boiling_point_c": 198,
            "geraniol_boiling_point_c": 230,
            "warning": "Drop before 206°C to preserve linalool"
        },
        
        "profile_targets": {
            "charge_temp_c": (195, 200),
            "gas_application": "Moderate (not aggressive)",
            "maillard_duration_min": (4, 5),
            "development_duration_min": (1.8, 2.2),
            "total_time_min": (10, 12)
        }
    },
    
    "brewing": {
        "pour_over_v60": {
            "dose_g": 20,
            "water_g": 340,
            "ratio": "1:17",  # Wider for delicate body
            "temp_c": (93, 95),
            "grind_comandante": (23, 25),
            "time_min": (3.0, 3.5),
            "note": "Highlight florals, avoid over-extraction"
        },
        
        "drip_on_ice": {
            "dose_g": 30,
            "hot_water_g": 220,
            "ice_in_server_g": 80,
            "total_yield_g": 300,
            "ratio": "1:11",  # Slightly wider for Geisha
            "temp_c": (94, 96),
            "grind_comandante": (21, 23),
            "time_min": (2.5, 3.0),
            "flavor_impact": "EXCEPTIONAL — floral aromatics locked by instant chill",
            "chemistry": "Volatile linalool (jasmine) trapped at 5°C, prevented from evaporating"
        },
        
        "cupping": {
            "temp_c": 93,
            "ratio": "1:18",
            "note": "Industry standard for evaluation"
        }
    },
    
    "economics": {
        "green_price_usd_per_kg": (20, 100),  # Can exceed $1,000 at auction
        "premium_vs_commodity_percent": (500, 2000),
        
        "auction_history": {
            "best_of_panama_2023_usd_per_kg": 1029,  # Elida Estate
            "typical_premium_geisha_usd_per_kg": (25, 50)
        },
        
        "farmer_perspective": {
            "pros": ["Extreme premium", "Prestige", "Market differentiation"],
            "cons": [
                "Very low yield",
                "Very high disease risk",
                "Very high labor",
                "Very specific terroir requirements"
            ],
            "break_even": "Need $30+/kg to justify vs Caturra",
            "critical": "MUST have confirmed premium buyer BEFORE planting"
        }
    },
    
    "alternative_slowbar_verdict": {
        "quality_rating": "10/10 (when everything aligns)",
        "yield_rating": "1/10",
        "disease_risk_rating": "10/10",
        "hype_vs_reality": "7/10",
        
        "honest_assessment": """
Geisha at auction = Speculation (not always value)
Geisha from skilled farmer at great terroir = Worth every penny
Geisha from average farm at wrong altitude = Wasted money

PLANT GEISHA ONLY IF:
  1. Altitude >1,500 masl (non-negotiable)
  2. Premium buyer confirmed ($30+/kg contracted)
  3. Disease management expertise + budget
  4. Can afford 50% lower yield
  5. Climate suits (cool, high rainfall)

If ANY above is "no" → Plant something else

BUYING GEISHA:
  - Panama/Colombia 1,700+ masl = Usually excellent
  - Low altitude / wrong climate = Overpaying for mediocrity
  - ALWAYS blind taste first, pay after
        """
    }
}
```

---

## ☕ BOURBON — The Balanced Classic

```python
bourbon_family = {
    "red_bourbon": {
        "genetics": {
            "origin": "Réunion island (formerly Île Bourbon), 1700s",
            "mutation_from": "Typica (spontaneous)",
            "genetic_difference": "Minor (natural selection)"
        },
        
        "morphology": {
            "tree_height_m": (2.5, 3.0),  # Shorter than Typica
            "branch_angle_degrees": (60, 80),
            "cherry_color": "Red when ripe",
            "bean_shape": "Round (vs Typica's narrow)",
            "screen_size": (16, 18)
        },
        
        "agronomy": {
            "yield_kg_per_ha": (1500, 2000),
            "yield_rating": "5/10 (MEDIUM)",
            "yield_vs_typica_percent": +30,
            
            "disease_resistance": {
                "coffee_leaf_rust": "2/10 (LOW but better than Typica)",
                "coffee_berry_disease": "3/10 (LOW)"
            },
            
            "climate": {
                "optimal_temp_c": (18, 23),
                "altitude_masl": (1000, 2000),
                "rainfall_mm": (1500, 2500)
            }
        },
        
        "chemistry": {
            "sugars_percent": (9.5, 11.5),  # Higher than Typica
            "caffeine_percent": (1.2, 1.5),
            "chlorogenic_acids_percent": (6, 8),
            "lipids_percent": (16, 18),
            
            "organic_acids": {
                "citric": "MEDIUM-HIGH",
                "malic": "MEDIUM-HIGH",
                "balance": "Excellent (not too bright, not flat)"
            }
        },
        
        "flavor_profile": {
            "acidity": "Medium-high, balanced",
            "body": "Medium, creamy",
            "sweetness": "High (caramel, brown sugar)",
            "complexity": "Good (fruity, balanced)",
            "notes": ["Stone fruit", "Caramel", "Chocolate", "Nuts"]
        },
        
        "brewing": {
            "pour_over": {
                "ratio": "1:15-1:16",  # Tighter for body
                "temp_c": (92, 94),
                "grind_comandante": (22, 24),
                "time_min": (2.75, 3.25),
                "note": "Sweeter than Typica, fuller body"
            },
            
            "drip_on_ice": {
                "dose_g": 30,
                "hot_water_g": 220,
                "ice_g": 80,
                "ratio": "1:10",
                "temp_c": (93, 95),
                "grind_comandante": (20, 22),
                "flavor": "Balanced sweetness + brightness, very approachable"
            }
        },
        
        "economics": {
            "green_price_usd_per_kg": (3.5, 7.0),
            "premium_vs_commodity_percent": (40, 100),
            "market_segment": "Specialty (82-85 SCA)"
        }
    },
    
    "yellow_bourbon": {
        "genetics": {
            "origin": "Brazil (natural mutation from Red Bourbon)",
            "mutation": "Recessive gene for yellow cherry"
        },
        
        "chemistry": {
            "sugars_percent": (10, 12),  # Higher than Red
            "note": "Sweeter profile, less acidity"
        },
        
        "flavor_profile": {
            "acidity": "Medium (lower than red)",
            "body": "Medium-full, syrupy",
            "sweetness": "Very high (honey, sugar cane)",
            "notes": ["Yellow fruit", "Honey", "Cream", "Vanilla"]
        },
        
        "processing_recommendation": {
            "natural": "EXCELLENT (high sugar content)",
            "honey": "EXCELLENT",
            "washed": "Good but wastes sweetness potential"
        },
        
        "brewing": {
            "drip_on_ice": {
                "note": "ESPECIALLY GOOD — natural sweetness + chill = perfection",
                "ratio": "1:10",
                "ice_g": 100,  # More ice for Brazil climate
                "flavor": "Honey sweetness, tropical fruit, cream"
            }
        }
    },
    
    "alternative_slowbar_verdict": {
        "quality_rating": "8/10",
        "yield_rating": "5/10",
        "disease_risk_rating": "7/10",
        "farmer_viability": "7/10",
        
        "assessment": """
Bourbon = The "safe" quality choice
  - Better yield than Typica (+30%)
  - Better quality than Catuai/Caturra
  - Disease risk still high (need management)
  - Market loves it (name recognition)

Yellow Bourbon specifically:
  - BEST for natural processing (high sugar)
  - Brazilian terroir optimized for it
  - Sweet, approachable cup (beginner-friendly)
  - EXCELLENT for Drip on Ice (Thailand market)

Recommendation: Start here if new to specialty
        """
    }
}
```

---

## 📊 VARIETY SELECTION MATRIX

```python
variety_selection_guide = {
    "by_goal": {
        "maximum_quality": {
            "varieties": ["Geisha", "SL28/34", "Ethiopian Heirlooms", "Typica", "Bourbon"],
            "requirements": ["High altitude", "Premium market", "Disease management"],
            "expected_premium_percent": (50, 500)
        },
        
        "balance_quality_yield": {
            "varieties": ["F1 Hybrids", "Bourbon", "Caturra", "Pacamara"],
            "requirements": ["Moderate altitude", "Specialty market"],
            "expected_premium_percent": (30, 100)
        },
        
        "maximize_yield": {
            "varieties": ["Catuai", "Castillo", "Mundo Novo"],
            "requirements": ["Good farming", "Consistent market"],
            "expected_premium_percent": (10, 50)
        },
        
        "disease_resistance": {
            "varieties": ["F1 Hybrids", "Castillo", "Ruiru 11", "Batian"],
            "requirements": ["Rust-prone areas"],
            "expected_premium_percent": (20, 60)
        }
    },
    
    "by_region": {
        "thailand": {
            "north_chiang_mai_chiang_rai": {
                "altitude_masl": (800, 1400),
                "recommended": ["Catimor", "Caturra", "Catuai", "Bourbon"],
                "climate_challenge": "Moderate altitude, heat tolerance needed",
                "expected_premium_percent": (10, 40)
            },
            "specialty_potential": {
                "altitude_masl": (1200, 1400),
                "recommended": ["Bourbon", "Caturra", "SL28 (trial)"],
                "note": "Limited high-altitude areas, maximize existing sites"
            }
        },
        
        "ethiopia": {
            "recommended": ["Ethiopian Heirlooms", "Geisha (from Gesha village)"],
            "avoid": "Imported varieties (heirlooms are superior)"
        },
        
        "kenya": {
            "recommended": ["SL28", "SL34", "Ruiru 11", "Batian"],
            "note": "SL28/34 = Kenya's signature, don't compete with others"
        },
        
        "panama": {
            "geisha_regions": ["Boquete", "Volcán"],
            "altitude_required": (1500, 2000),
            "note": "Geisha heartland, but market saturated"
        }
    }
}
```

---

## 🌡️ ROASTING MATRIX BY VARIETY

```python
roasting_matrix = {
    "high_density_varieties": {
        "list": ["Geisha", "SL28/34", "Ethiopian@1800masl", "Typica@1500+"],
        "bean_density_g_per_cm3": (0.70, 0.78),
        
        "adjustments": {
            "charge_temp_c": "+5 to +10 vs standard",
            "first_crack_expected_c": (198, 205),
            "development_time_min": (2.0, 2.5),
            "total_time_min": (10, 12),
            "rationale": "Dense beans = more thermal mass = need more energy"
        }
    },
    
    "low_density_varieties": {
        "list": ["Catimor@<1000masl", "Robusta", "Low-altitude lots"],
        "bean_density_g_per_cm3": (0.60, 0.68),
        
        "adjustments": {
            "charge_temp_c": "-5 vs standard",
            "first_crack_expected_c": (192, 198),
            "development_time_min": (1.5, 2.0),
            "total_time_min": (8, 10),
            "rationale": "Less dense = faster heat absorption = risk of baking if slow"
        }
    },
    
    "large_bean_varieties": {
