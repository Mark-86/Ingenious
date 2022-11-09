import Link from "next/link";
import { useState } from "react";
import axios from "axios";
import { useRouter } from "next/router";

export default function signup() {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");

  const router = useRouter();

  const handleSubmit = async (event) => {
    event.preventDefault();

    try {
      const response = await axios.post("http://localhost:8000/auth/register", {
        email,
        password,
      });
      router.replace("/codeground");
    } catch (err) {
      alert(err.response.data.detail);
    }
  };
  return (
    <section className="h-screen bg-bgPrimary flex items-center justify-center">
      <form
        className="flex flex-col rounded-2xl shadow-2xl items-center justify-center gap-y-10 bg-bgSecondary w-[500px] h-[600px]"
        onSubmit={handleSubmit}
      >
        <h3 className=" font-extrabold tracking-widest text-transparent text-5xl pb-10 bg-clip-text bg-gradient-to-r from-purple-400 to-pink-600 drop-shadow-xl">
          Sign Up
        </h3>
        <div>
          <input
            className="px-5 text-white py-3 rounded-3xl bg-bgPrimary drop-shadow-2xl"
            id="name"
            type={"email"}
            value={email}
            onChange={(e) => setEmail(e.target.value)}
            placeholder="Email"
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
          // bg-gradient-to-r text-white from-primary to-secondary
          className="gradientBg text-white px-20 py-5 rounded-3xl drop-shadow-xl font-extrabold text-xl tracking-widest "
          type={"submit"}
        >
          Submit
        </button>
        <p className="text-white/60">
          Already have an account?
          <Link href={"/auth"}>
            <span className="underline pl-1 cursor-pointer">Login</span>
          </Link>
        </p>
      </form>
    </section>
  );
}
