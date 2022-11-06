import Link from "next/link";
import { useState } from "react";
import { useRouter } from "next/router";

export default function AuthPage() {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");

  const router = useRouter();

  const handleSubmit = (event) => {
    event.preventDefault();
    console.log(username, password);
    router.replace("codeground");
  };

  return (
    <section className="h-screen bg-bgPrimary flex items-center justify-center">
      <form
        className="flex flex-col rounded-2xl shadow-2xl items-center justify-center gap-y-10 bg-bgSecondary w-[500px] h-[600px]"
        onSubmit={handleSubmit}
      >
        <h3 className=" font-extrabold tracking-widest text-transparent text-5xl pb-10 bg-clip-text bg-gradient-to-r from-purple-400 to-pink-600 drop-shadow-xl">
          Login
        </h3>
        <div>
          <input
            className="px-5 text-white py-3 rounded-3xl bg-bgPrimary drop-shadow-2xl"
            id="name"
            value={username}
            onChange={(e) => setUsername(e.target.value)}
            type={"text"}
            placeholder="Username"
          />{" "}
        </div>
        <div>
          <input
            className="px-5 py-3 text-white rounded-3xl bg-bgPrimary drop-shadow-2xl"
            id="name"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            type={"password"}
            placeholder="Password"
          />
        </div>
        <button
          className="text-white gradientBg px-20 py-5 rounded-3xl drop-shadow-xl font-extrabold text-xl tracking-widest "
          type={"submit"}
        >
          Submit
        </button>
        <p className="text-white/60">
          New to our platform?{" "}
          <Link href={"/auth/signup"}>
            <span className="underline cursor-pointer">Sign Up!</span>
          </Link>
        </p>
      </form>
    </section>
  );
}
