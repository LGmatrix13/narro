document.addEventListener("DOMContentLoaded", async () => {
  const likeButton = document.getElementById("like-button");
  likeButton.addEventListener("click", async () => {
    const postId = document.getElementById("post-id").value;
    const r = await fetch(`/post/${postId}`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
    });

    if (r.ok) {
      const likeButton = document.getElementById("like-button");
      const likeCount = document.getElementById("like-count");
      const postLiked = likeButton.innerText === "Unlike Story";

      if (postLiked) {
        likeButton.innerText = "Like Story";
        likeButton.className = "bg-blue-600 text-white w-full rounded-lg p-3";
        likeCount.innerText = `${
          Number(likeCount.innerText.split(" ")[0]) - 1
        } Likes`;
      } else {
        likeButton.innerText = "Unlike Story";
        likeButton.className =
          "bg-slate-50/[0.06] text-white w-full rounded-lg p-3";
        likeCount.innerText = `${
          Number(likeCount.innerText.split(" ")[0]) + 1
        } Likes`;
      }
    }
  });
});
