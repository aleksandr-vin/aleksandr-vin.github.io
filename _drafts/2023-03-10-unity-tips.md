---
title: "Unity tips"
tags: unity, tips
---

# Random tips

1. [Edit the playmode tint color](https://learn.unity.com/tutorial/1-3-make-the-camera-follow-the-vehicle-with-variables?uv=2021.3&labelRequired=true&pathwayId=5f7e17e1edbc2a5ec21a20af&missionId=5f71fe63edbc2a00200e9de0&projectId=5caccdfbedbc2a3cef0efe63#63b4e387edbc2a49cf9ed999)

2. [Introduction to project management and teamwork](https://learn.unity.com/tutorial/introduction-to-project-management-and-teamwork?uv=2021.3&pathwayId=5f7e17e1edbc2a5ec21a20af&missionId=5f71fe63edbc2a00200e9de0#5fad668fedbc2a002016e0ad)

3. _GameManager.cs_ script and _Game Manager_ Empty Object.

   See [lesson](https://learn.unity.com/tutorial/lesson-5-1-clicky-mouse?uv=2021.3&pathwayId=5f7e17e1edbc2a5ec21a20af&missionId=5f7648a4edbc2a5578eb67df&projectId=5cf96bdeedbc2a2b475972b3#).

   and then

   ```
   gameManager = GameObject.Find("Game Manager").GetComponent<GameManager>();
   ```

   from [lesson](https://learn.unity.com/tutorial/lesson-5-2-keeping-score?uv=2021.3&pathwayId=5f7e17e1edbc2a5ec21a20af&missionId=5f7648a4edbc2a5578eb67df&projectId=5cf96bdeedbc2a2b475972b3#5ce6151aedbc2a0076e7401a).

4. Getting *Rigidbody* for **self**

   ```
   targetRb = GetComponent<Rigidbody>();
   ```

   See [lesson](https://learn.unity.com/tutorial/lesson-5-1-clicky-mouse?uv=2021.3&pathwayId=5f7e17e1edbc2a5ec21a20af&missionId=5f7648a4edbc2a5578eb67df&projectId=5cf96bdeedbc2a2b475972b3#).

5. Coroutines `StartCoroutine`

   See [lesson](https://learn.unity.com/tutorial/lesson-5-1-clicky-mouse?uv=2021.3&pathwayId=5f7e17e1edbc2a5ec21a20af&missionId=5f7648a4edbc2a5578eb67df&projectId=5cf96bdeedbc2a2b475972b3#).

6. *GameObject* of **self** is just `gameObject`

   See [lesson](https://learn.unity.com/tutorial/lesson-5-1-clicky-mouse?uv=2021.3&pathwayId=5f7e17e1edbc2a5ec21a20af&missionId=5f7648a4edbc2a5578eb67df&projectId=5cf96bdeedbc2a2b475972b3#).

7. *ParticleSystem*

   Make it public, assign in GUI, and call `Instantiate` when needed. See [lesson](https://learn.unity.com/tutorial/lesson-5-2-keeping-score?uv=2021.3&pathwayId=5f7e17e1edbc2a5ec21a20af&missionId=5f7648a4edbc2a5578eb67df&projectId=5cf96bdeedbc2a2b475972b3#5ce6151aedbc2a0076e7401a).

8. *Canvas* and *Text Mesh Pro* and *Anchor Points*

   See [lesson](https://learn.unity.com/tutorial/lesson-5-2-keeping-score?uv=2021.3&pathwayId=5f7e17e1edbc2a5ec21a20af&missionId=5f7648a4edbc2a5578eb67df&projectId=5cf96bdeedbc2a2b475972b3#).

9. `AddListener` on buttons

   See [lesson](https://learn.unity.com/tutorial/lesson-5-4-what-s-the-difficulty?uv=2021.3&pathwayId=5f7e17e1edbc2a5ec21a20af&missionId=5f7648a4edbc2a5578eb67df&projectId=5cf96bdeedbc2a2b475972b3#).
   
10. Nested Prefabs

   See [lesson](https://learn.unity.com/tutorial/lab-5-swap-out-your-assets-1?uv=2021.3&pathwayId=5f7e17e1edbc2a5ec21a20af&missionId=5f7648a4edbc2a5578eb67df&projectId=5cf96bdeedbc2a2b475972b3#).

11. Persist volume level between restarts (scene reloads)

    Use static variable to store the value.
