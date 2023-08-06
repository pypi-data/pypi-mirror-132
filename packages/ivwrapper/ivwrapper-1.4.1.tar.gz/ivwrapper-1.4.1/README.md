# ivwrapper 1.4.1
Asynchroniczny wrapper dla api ivall'a.

## Instalacja

Możesz zainstalować bibliotekę prosto z pypi

**Instalacja:** `pip install ivwrapper`<br>

## Przykładowe użycie
```python
import asyncio
import ivwrapper

iv = ivwrapper.Api()


async def main():
    joke = await iv.get_joke()
    print(joke)


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())

```
## Endpoint'y
```python
# endpoint'y
await get_joke()  # Losuje randomowy żart
await get_meme() # Losuje randomowy mem
 ```