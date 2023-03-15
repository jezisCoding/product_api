[+]
 
### Obecné
    - aplikace šla spustit
    - readme
    - databázové schéma
    - notes, known bugs - fajn

### Funkčnost

    - [POST] /import
        - hlídání povinných polí
        - např. u produktu by dávalo smysl ještě: název, měna
        - update modelů
        - správný status kód na create
        - lze zadávat více modelů zároveň
        - hlídání existence cizích klíčů
        - hlídání datových typů polí

    - [GET] /detail & /detail/{ID}
        - hlídání nexistujícího názvu modelu
        - ok

### Kód a struktura
    - docstrings fajn

    - models
      - u CharFieldů default="" fajn
      - využití DecimalField pro cenu
      - využití ForeignKey a ManyToManyField
    - serializers
      - využití to_representation a update metod
      - update many-to-many hodnot v CatalogSerializer
    - views 
        - navíc [DELETE] view + správný status kód
        - [POST] /import/ 
          - fajn, že máš vyspecifikované modely a serializéry v dicts a tady je používáš
            dynamicky
            - ještě lepší by bylo nechat třeba jen jeden dict na jednom místě, kde bys měl model classy
              a serializer classy (název modelu/serializéru si můžeš vytáhnout např. Model.__name__)
          - správné flow - kontrola existence instance, validace dat, uložení nebo chyba
        - [GET] /detail & /detail/{ID}
          - validace neexistujícího modelu
          - dynamické načtení serializéru


[-]

### Obecné  
    - requirements
      - pkg_resources==0.0.0 způsobovali chybu při instalaci
      - (drobnost) django-rest-framework==0.1.0 je nějaký package na pypi, ale není to rest framework, takže
        ten raději neinstalovat MAM
    - (drobnost) možná až moc souborů v root adresáři, test data bych dal do adresáře test
      db a notes třeba do adresáře docs MAM
    - (drobnost) apina je cool název :), ale spíš bych nechal jen api 

### Funkčnost

    - [POST] /import
        - na zadání chybného názvu modelu vrací api 500 internal server error done
        - na zadání dictu jako root elementu (namísto list) taktéž 500 internal server error done
        - když nezadáme "id", taktéž 500 internal server error done
        - (malá chyba) na update také vracíš 201 created status kód, na update lepší 200 done
        - foreign keys by neměly jít zadat prázdné (kromě asi obrazek_id v Catalog)

    - [GET] /detail & /detail/{ID}
        - nelze vrátit data pro ProductAttributes model (Object of type Attribute is not JSON serializable) mam
        - (malá chyba) u neexistujícího ID bych spíše vrátil 404 status message, ale 400 není úplně špatně
        - (malá chyba) při vrácení dat už bych nezdůrazňoval v reponse
          opět název modelu, ten je už v URL

### Kód a struktura
    - (malá chyba) PEP 8 - formátování, mezi classami by měly být 2 mezery
    - mohli být i nějaké testy

    - models
      - některé pole, např. nazev, kod u AttributName by mohli být delší než 15 znaků mam
      - (malá chyba) dobré je dávat __str__ a Meta class pro modely mam
      - cizí klíče by neměly být null=True, možná až na obrazek_id v Catalog
        modelu, protože ostatní modely tvoří mezitabulku v M2M vazbě, takže not null
        je zde nutnost
      - (menší chyba) u BooleanField taky moc nedává smysl null=True, spíše
        lepší nějaký default mam
      - (malá chyba) u mezitabulek nebo Attribute modelu je lepší dát u ForeignKeys's
        on_delete=CASCADE mam
      - (malá chyba) id field bys zde ani nemusel specifikovat a nechat djangovský
        build in
      - (drobnost) cizí kliče a many to many je lepší nazývat bez toho id a ids,
        i když v DB to jsou vlastně ID, když s tím pracuješ v djangu, dostáváš
        už rovnou instance, např. catalog.products.all() mam
    - serializers
      - (menší chyba) lepší by bylo vyspecifikovat fieldy na úrovni
        serializérů a ne v to_representation method, název modelu,
        který si zde zřejmě potřeboval bych doplnil ve view
      - (menší chyba) chápu, že v CatalogSerializer ručně updatuješ i nazev a obrazek_id,
        ale když to necháš takto, aplikace při pokusu o update spadne, protože ji nikde
        neukládáš, tedy chtělo by to item.save() na konci 
          - nebo tady můžeš využít např. super().save(item, validated_data), což
            by ti zařídilo update jednoduchý polí (i které bys pak do modelu přidal) 
    - urls - (menší chyba) máš zduplikované ursl všechny
    - views 
        - [POST] /import/
          - (drobnost) lepší využít update_or_create metodu djanga, ale jinak to máš správně
          - zde nehlídáš, jestli název modelu existuje v my_models done
            - využít try/except done
          - taky bys mohl hlídat formát příchozích dat, jeslti jsou v listu a ne třeba v dictu
            - využít try/except
        - [GET] /detail & /detail/{ID} done
          - (menší chyba) mohl by si hlídat neexistující název modelu i v detailu/{ID} done

# Tvé otázky v notes
1) je pravda, že nemáš delete endoint, ale určitě pro mezitabulky nebo Attribute model je lepší
   mít CASCADE (v praxi pak téměř vždy existuje delete)
2) určitě je lepší ty pole přepsat všechny
3) status 200, klidně bych ten model vrátil se všemi daty, aby bylo vidět, co se změnilo